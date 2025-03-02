from collections import namedtuple
from queue import Queue
from typing import Callable

from hephaestus.io import get_logger
from hephaestus.patterns import Singleton

_logger = get_logger(__name__)

##
# Public
##
MethodTrace = namedtuple("MethodTrace", ["name", "args", "kwargs", "retval"])


class TraceQueue(Queue, metaclass=Singleton):
    """An object capable of storing method calls and other trace information."""

    def get(self) -> MethodTrace:
        """Returns the last trace.

        Returns:
            The last method trace containing the method's name, the passed
            positional arguments, keyword arguments, and returned value, if any.
        """
        retval = None if self.empty() else super().get()

        return retval

    def clear(self):
        """Removes all MethodTraces from memory."""
        _logger.debug("Clearing trace queue.")
        while not self.empty():
            _ = self.get()


def trace(to_trace: Callable) -> Callable:
    """Records method call for later examination.

    Args:
        to_trace : the method to trace.

    Returns:
        The passed method with minor modifications to support tracing capability.

    Note:
        Can be used as a decorator:

        @trace
        def print_copy(*args):
            ...

        Or like a regular method:

        print_copy = trace(to_trace=print_copy)

    """

    def wrapper(*args, **kwargs):
        """Forward all method parameters to wrapped method."""
        _logger.debug(
            f"Traced method: {to_trace.__name__}, Args: {args}, Keyword Args: {kwargs}"
        )

        # Call method and store in queue.
        retval = to_trace(*args, **kwargs)
        TraceQueue().put(
            MethodTrace(name=to_trace.__name__, args=args, kwargs=kwargs, retval=retval)
        )

        _logger.debug(f"Method returned. Return value: {retval}")
        return retval

    return wrapper
