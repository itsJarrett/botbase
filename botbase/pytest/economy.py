import pytest

__all__ = ["bank"]


@pytest.fixture()
def bank(config, monkeypatch):
    from botbase.core import Config

    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        from botbase.core import bank

        bank._register_defaults()
        return bank
