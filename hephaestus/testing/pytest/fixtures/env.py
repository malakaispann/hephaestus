import pytest

from hephaestus.patterns import Singleton


@pytest.fixture(scope="function", autouse=True)
def reset_env():
    """Resets Hephaestus memory and such after each test."""
    yield

    # Reset any shared memory
    Singleton.clear_all()
