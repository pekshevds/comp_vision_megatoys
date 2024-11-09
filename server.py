from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File, Request, Body
from fastapi.responses import HTMLResponse, Response
from settings import templates, PHOTO_NAME
from services import save_file, save_photo
from services.cv import prepare_image, fetch_faces_from_image, get_name_by_faces
from services.camera import get_photo_from_camera


app = FastAPI()


class CameraSettings(BaseModel):
    ip: str
    username: str
    password: str


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "index"},
    )


@app.post("/get-mask-from-file")
def get_mask_by_image_from_file(file: UploadFile = File(...)):
    save_file(file, PHOTO_NAME)
    image = prepare_image(PHOTO_NAME)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}


@app.get("/get-mask-from-camera")
def get_mask_by_image_from_camera(camera_settings: Annotated[CameraSettings, Body()]):
    save_photo(
        get_photo_from_camera(
            camera_settings.ip,
            camera_settings.username,
            camera_settings.password,
        ),
        PHOTO_NAME,
    )
    image = prepare_image(PHOTO_NAME)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}


@app.get("/get-image-from-camera")
def get_image_from_camera(camera_settings: Annotated[CameraSettings, Body()]):
    return Response(
        get_photo_from_camera(
            camera_settings.ip,
            camera_settings.username,
            camera_settings.password,
        ),
        media_type="image/jpg",
    )
