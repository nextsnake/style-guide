from astroid import nodes
from pylint.checkers import BaseChecker, utils
from pylint.interfaces import IAstroidChecker


class AsyncIOChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "asyncio-best-practices"
    msgs = {
        "R9410": (
            "Using deprecated asyncio.get_event_loop. Use asyncio.get_current_loop instead.",
            "asyncio-get-event-loop",
            "Usage of get_current_loop is preferred due to various potential issues with get_event_loop. "
            "https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop",
        ),
    }

    def visit_call(self, node: nodes.Call) -> None:
        for inferred in utils.infer_all(node.func):
            if not isinstance(inferred, nodes.FunctionDef):
                continue

            if inferred.qname() == "asyncio.events.get_event_loop":
                self.add_message("asyncio-get-event-loop", node=node)
