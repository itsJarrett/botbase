import pytest

from botbase.cogs.alias import Alias
from botbase.core import Config

__all__ = ["alias"]


@pytest.fixture()
def alias(config, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        return Alias(None)
