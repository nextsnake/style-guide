from __future__ import annotations

from typing import TYPE_CHECKING

from .get_event_loop_check import GetEventLoopChecker
from .license_check import LicenseChecker
from .old_typing_check import OldTypingChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: PyLinter):
    linter.register_checker(GetEventLoopChecker(linter))
    linter.register_checker(LicenseChecker(linter))
    linter.register_checker(OldTypingChecker(linter))
