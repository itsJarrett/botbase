import pytest

__all__ = ["mod"]


@pytest.fixture
def mod(config, monkeypatch):
    from botbase.core import Config

    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        from botbase.core import modlog

        modlog._register_defaults()
        return modlog
