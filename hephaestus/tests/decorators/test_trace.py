import hephaestus.testing.swte as swte
from hephaestus.decorators import trace, TraceQueue


class Testtrace:

    FAKE_FUNCTION_RETURN_VALUE = 5

    def _fake_function(self, *args, **kwargs):
        return self.FAKE_FUNCTION_RETURN_VALUE

    def test_trace_function(
        self,
    ):
        """Verifies trace method successfully captures a method call and associated information."""

        tq = TraceQueue()

        wrapped_fake_function = trace(self._fake_function)
        wrapped_fake_function()

        assert tq.get().name == self._fake_function.__name__

    def test_trace_arguments(self):
        """Verifies traceer records the arguments passed to a method."""

        args = (swte.IntConsts.BADDCAFE, swte.IntConsts.DEADBEEF)
        kwargs = {
            "DEADBEEF": swte.StrConsts.DEADBEEF,
            "BADDCAFE": swte.StrConsts.BADDCAFE,
        }

        tq = TraceQueue()

        wrapped_fake_function = trace(self._fake_function)
        wrapped_fake_function(*args, **kwargs)

        traced = tq.get()
        assert traced.args == args and traced.kwargs == kwargs

    def test_trace_return_value(self):
        """Verifies trace method successfully records the return value of a method"""

        tq = TraceQueue()

        wrapped_fake_function = trace(self._fake_function)
        wrapped_fake_function()

        assert tq.get().retval == self.FAKE_FUNCTION_RETURN_VALUE
