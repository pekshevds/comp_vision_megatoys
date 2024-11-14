import pytest
from typing import Any
from mock import patch
from utils.camera import CameraSettings, get_photo_from_camera


@pytest.fixture
def fake_camera_settings() -> CameraSettings:
    cs = CameraSettings(ip="172.0.0.1", username="user", password="password")
    return cs


@pytest.fixture
def fake_camera_content() -> Any:
    return b"some binary data"


def test__get_photo_from_camera__return_none(
    fake_camera_settings: CameraSettings,
) -> None:
    with patch("utils.camera.get_data_from_camera") as mock_get_data_from_camera:
        mock_get_data_from_camera.return_value = None
        assert get_photo_from_camera(fake_camera_settings) is None


def test__get_photo_from_camera__return_binary_data(
    fake_camera_settings: CameraSettings, fake_camera_content: Any
) -> None:
    with patch("utils.camera.get_data_from_camera") as mock_get_data_from_camera:
        mock_get_data_from_camera.return_value = fake_camera_content
        assert get_photo_from_camera(fake_camera_settings) is fake_camera_content
