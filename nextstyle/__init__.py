from __future__ import annotations

from typing import TYPE_CHECKING

from .asyncio_check import AsyncIOChecker
from .license_check import LicenseChecker
from .old_typing_check import OldTypingChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: PyLinter):
    linter.register_checker(AsyncIOChecker(linter))
    linter.register_checker(LicenseChecker(linter))
    linter.register_checker(OldTypingChecker(linter))
