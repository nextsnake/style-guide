from __future__ import annotations

import itertools
from pathlib import Path
from typing import TYPE_CHECKING

from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class LicenseChecker(BaseChecker):
    __implements__ = IRawChecker

    name = "license"
    msgs = {
        "R9415": (
            "Module license header is invalid or missing.",
            "invalid-license",
            "See ./license_header.txt",
        ),
    }

    def __init__(self, linter: PyLinter | None = None) -> None:
        super().__init__(linter)
        license_path = Path(__file__).parent / "license_header.txt"
        self._license_text = license_path.read_bytes().splitlines()

    def process_module(self, node: nodes.Module) -> None:
        with node.stream() as stream:
            header_gen = itertools.islice(stream, len(self._license_text))
            if self._license_text != [line.rstrip() for line in header_gen]:
                self.add_message("invalid-license", line=0)
