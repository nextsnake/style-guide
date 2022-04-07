from typing import TYPE_CHECKING, Optional

import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class OldTypingChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "unique-returns"
    msgs = {
        "R9401": (
            "Outdated typing! Please use dict instead of typing.Dict",
            "outdated-typing-dict",
            "These can be replaced from typing.Dict[int] to dict[int]. You may need to add `from __future__ import annotations` to your imports if you plan on supporting Python 3.8-.",
        ),
        "R9402": (
            "Outdated typing! Please use list instead of typing.List",
            "outdated-typing-list",
            "These can be replaced from typing.List[int] to list[int]. You may need to add `from __future__ import annotations` to your imports if you plan on supporting Python 3.8-.",
        ),
        "R9403": (
            "Outdated typing! Please use <t1> | <t2> instead of typing.Union",
            "outdated-typing-union",
            "These can be replaced from typing.Union[int, str] to int | str. You may need to add `from __future__ import annotations` to your imports if you plan on supporting Python 3.10-.",
        ),
        "R9404": (
            "Outdated typing! Please use tuple instead of typing.Tuple",
            "outdated-typing-tuple",
            "These can be replaced from typing.Tuple[int] to tuple[int]. You may need to add `from __future__ import annotations` to your imports if you plan on supporting Python 3.8-.",
        ),
        "R9405": (
            "Outdated typing! Please use t1 | None instead of typing.Optional",
            "outdated-typing-optional",
            "These can be replaced from typing.Optional[int] to int | None. You may need to add `from __future__ import annotations` to your imports if you plan on supporting Python 3.8-.",
        ),
    }
    options = (
        (
            "ignore-ints",
            {
                "default": False,
                "type": "yn",
                "metavar": "<y or n>",
                "help": "Allow returning non-unique integers",
            },
        ),
    )

    def visit_importfrom(self, node: nodes.ImportFrom) -> None:
        if node.modname == "typing":
            for name, _ in node.names:
                if name == "Dict":
                    self.add_message("outdated-typing-dict", node=node)
                elif name == "List":
                    self.add_message("outdated-typing-list", node=node)
                elif name == "Union":
                    self.add_message("outdated-typing-union", node=node)
                elif name == "Tuple":
                    self.add_message("outdated-typing-tuple", node=node)
                elif name == "Optional":
                    self.add_message("outdated-typing-optional", node=node)
