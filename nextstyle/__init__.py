from __future__ import annotations
from .old_typing_check import OldTypingChecker
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pylint.lint import PyLinter

def register(linter: PyLinter):
    linter.register_checker(OldTypingChecker(linter))

