from activate.activate_manager import get_activate_manager
import pytest


@pytest.fixture
def manager():
    yield get_activate_manager()


def test_manager_resolver(manager):
    @manager.resolver
    def to_be_decorated():
        return "BUG!"

    to_be_decorated("test")
    assert manager.schema.get("test") is not None
