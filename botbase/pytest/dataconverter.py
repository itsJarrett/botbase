from pathlib import Path

from botbase.cogs.dataconverter import core_specs

__all__ = ["get_specresolver"]


def get_specresolver(path):
    here = Path(path)

    resolver = core_specs.SpecResolver(here.parent)
    return resolver
