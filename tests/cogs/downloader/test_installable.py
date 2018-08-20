import json
from pathlib import Path

import pytest

from botbase.pytest.downloader import *
from botbase.cogs.downloader.installable import Installable, InstallableType


def test_process_info_file(installable):
    for k, v in INFO_JSON.items():
        if k == "type":
            assert installable.type == InstallableType.COG
        else:
            assert getattr(installable, k) == v


# noinspection PyProtectedMember
def test_location_is_dir(installable):
    assert installable._location.exists()
    assert installable._location.is_dir()


# noinspection PyProtectedMember
def test_info_file_is_file(installable):
    assert installable._info_file.exists()
    assert installable._info_file.is_file()


def test_name(installable):
    assert installable.name == "test_cog"


def test_repo_name(installable):
    assert installable.repo_name == "test_repo"


def test_serialization(installable):
    data = installable.to_json()
    cog_name = data["cog_name"]

    assert cog_name == "test_cog"
