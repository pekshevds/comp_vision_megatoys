import pytest
from typing import Any
from mock import patch
from utils.cv import prepare_image, fetch_masks_from_image, get_art_by_masks


@pytest.fixture
def fake_image() -> str:
    return cs
