"""Main entry point for CodeBuddy Telegram bot."""

from __future__ import annotations

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import Config
from bot.database import Database
from bot.handlers import register_handlers


def configure_logging(level_name: str) -> None:
    """Configure console logging with timestamps and log levels."""
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


async def main() -> None:
    """Initialize resources and launch bot polling."""
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
    await db.init_db()

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

    logger.info("Routers registered. Starting long polling...")

    try:
        retry_delay = 3
        while True:
            try:
                # Delete any pending webhook updates and start polling
                await bot.delete_webhook(drop_pending_updates=True)
                await dp.start_polling(bot)
                break
            except (KeyboardInterrupt, SystemExit):
                logger.info("Shutdown requested.")
                break
            except Exception as exc:
                logger.warning("Network/polling error: %s. Reconnecting in %s seconds...", exc, retry_delay)
                await asyncio.sleep(retry_delay)
                retry_delay = min(retry_delay * 2, 30)
    finally:
        logger.info("Closing bot session...")
        await bot.session.close()
        logger.info("CodeBuddy bot stopped cleanly.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
