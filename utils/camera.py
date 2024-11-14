import httpx
from typing import Any
from pydantic import BaseModel


class CameraSettings(BaseModel):
    ip: str
    username: str
    password: str


def get_data_from_camera(camera_url: str, username: str, password: str) -> Any | None:
    auth = httpx.DigestAuth(username=username, password=password)
    client = httpx.Client(auth=auth)
    try:
        response = client.get(camera_url)
    except httpx.ConnectTimeout:
        return None
    return response.content


def get_camera_url(ip: str) -> str:
    return f"http://{ip}/cgi-bin/snapshot.cgi"


def get_photo_from_camera(camera_settings: CameraSettings) -> Any | None:
    return get_data_from_camera(
        get_camera_url(camera_settings.ip),
        username=camera_settings.username,
        password=camera_settings.password,
    )
