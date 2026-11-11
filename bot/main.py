"""Main entry point for CodeBuddy Telegram bot."""

from __future__ import annotations

import asyncio
import logging
import sys

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from bot.config import Config
from bot.database import Database
from bot.handlers import register_handlers

WEBHOOK_PATH = "/webhook"


def configure_logging(level_name: str) -> None:
    """Configure console logging with timestamps and log levels."""
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


async def setup_bot_commands(bot: Bot) -> None:
    """Configure Telegram native menu commands."""
    logger = logging.getLogger("codebuddy")
    try:
        commands = [
            BotCommand(command="menu", description="🏠 Main Menu / ዋና ማውጫ"),
            BotCommand(command="tutor", description="🧑‍🏫 Interactive Tutor / የግል አስተማሪ"),
            BotCommand(command="learn", description="📚 Lessons & Curriculum / ትምህርቶች"),
            BotCommand(command="practice", description="💻 Practice Arena / ልምምድ"),
            BotCommand(command="codelab", description="🔬 CodeLab Sandbox / ኮድ መጻፊያ"),
            BotCommand(command="settings", description="⚙️ Language & Settings / ቅንብሮች"),
            BotCommand(command="help", description="ℹ️ Help & Commands / እገዛ"),
        ]
        await bot.set_my_commands(commands)
        logger.info("Telegram command menu registered successfully.")
    except Exception as cmd_err:
        logger.warning("Could not set Telegram commands: %s", cmd_err)


async def health_check(request: web.Request) -> web.Response:
    """Health check endpoint for Render free tier monitoring."""
    return web.Response(text="OK\n", content_type="text/plain")


async def root_handler(request: web.Request) -> web.Response:
    """Root info endpoint."""
    return web.Response(
        text="CodeBuddy Telegram Bot Webhook Server is live! Status: 200 OK\n",
        content_type="text/plain",
    )


def main() -> None:
    """Initialize resources and launch bot via Webhook (Render) or Polling (local)."""
    # 1. Load configuration
    try:
        config = Config.load()
    except Exception as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        sys.exit(1)

    # 2. Configure logging
    configure_logging(config.log_level)
    logger = logging.getLogger("codebuddy")
    logger.info("Starting CodeBuddy bot...")
    logger.info("Bot token loaded successfully (%s)", config.masked_token)

    # 3. Initialize SQLite database
    db = Database(config.database_path)

    # 4. Initialize Bot and Dispatcher
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Pass database instance to all handlers
    dp["db"] = db

    # 5. Register routers
    register_handlers(dp)

    if config.webhook_url and config.webhook_url.startswith("http"):
        # WEBHOOK MODE (Active on Render)
        webhook_full_url = f"{config.webhook_url.rstrip('/')}{WEBHOOK_PATH}"
        logger.info("Operating in Webhook mode. Target: %s, port: %s", webhook_full_url, config.port)

        async def on_startup(bot: Bot) -> None:
            await db.init_db()
            logger.info("Setting Telegram Webhook to %s ...", webhook_full_url)
            await bot.set_webhook(
                url=webhook_full_url,
                drop_pending_updates=False,
                allowed_updates=["message", "callback_query"],
            )
            await setup_bot_commands(bot)

        async def on_shutdown(bot: Bot) -> None:
            logger.info("Closing bot session...")
            await bot.session.close()

        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)

        app = web.Application()
        app.router.add_get("/", root_handler)
        app.router.add_get("/health", health_check)

        SimpleRequestHandler(
            dispatcher=dp,
            bot=bot,
        ).register(app, path=WEBHOOK_PATH)

        setup_application(app, dp, bot=bot)

        logger.info("Starting aiohttp Webhook server on 0.0.0.0:%s", config.port)
        web.run_app(app, host="0.0.0.0", port=config.port)

    else:
        # POLLING MODE (Fallback for local dev)
        logger.info("No webhook URL configured. Starting long polling...")

        async def run_polling():
            await db.init_db()
            await setup_bot_commands(bot)
            try:
                retry_delay = 3
                while True:
                    try:
                        await bot.delete_webhook(drop_pending_updates=False)
                        await dp.start_polling(bot)
                        break
                    except (KeyboardInterrupt, SystemExit):
                        logger.info("Shutdown requested.")
                        break
                    except Exception as exc:
                        logger.warning(
                            "Network/polling error: %s. Reconnecting in %s seconds...",
                            exc,
                            retry_delay,
                        )
                        await asyncio.sleep(retry_delay)
                        retry_delay = min(retry_delay * 2, 30)
            finally:
                logger.info("Closing bot session...")
                await bot.session.close()
                logger.info("CodeBuddy bot stopped cleanly.")

        asyncio.run(run_polling())


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        pass
