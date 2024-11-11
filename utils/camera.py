from typing import Any
import httpx


def get_photo_from_camera(ip: str, username: str, password: str) -> Any | None:
    url = f"http://{ip}/cgi-bin/snapshot.cgi"
    auth = httpx.DigestAuth(username=username, password=password)
    client = httpx.Client(auth=auth)
    try:
        response = client.get(url)
    except httpx.ConnectTimeout:
        return None
    return response.content
