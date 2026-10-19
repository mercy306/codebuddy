"""Handlers package."""

from aiogram import Dispatcher

from bot.handlers.start import router as start_router
from bot.handlers.help import router as help_router
from bot.handlers.learn import router as learn_router
from bot.handlers.practice import router as practice_router
from bot.handlers.codelab import router as codelab_router
from bot.handlers.tutor import router as tutor_router
from bot.handlers.menu import router as menu_router
from bot.handlers.fallback import router as fallback_router


def register_handlers(dp: Dispatcher) -> None:
    """Register all routers in priority order."""
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(learn_router)
    dp.include_router(practice_router)
    dp.include_router(codelab_router)
    dp.include_router(tutor_router)
    dp.include_router(menu_router)
    # Fallback router must always be last
    dp.include_router(fallback_router)
