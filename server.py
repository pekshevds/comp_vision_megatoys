from typing import Annotated, Any
from fastapi import FastAPI, UploadFile, File, Request, Body
from fastapi.responses import HTMLResponse, Response
from settings import templates, PHOTO_NAME
from utils import save_file, save_photo
from utils.cv import prepare_image, fetch_masks_from_image, get_art_by_masks
from utils.camera import CameraSettings, get_photo_from_camera


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "index"},
    )


@app.post("/get-mask-from-file")
def get_mask_by_image_from_file(file: UploadFile = File(...)) -> dict[str, Any]:
    save_file(file, PHOTO_NAME)
    image = prepare_image(PHOTO_NAME)
    if image is None:
        return {"result": "error"}
    masks = fetch_masks_from_image(image)
    if masks is None:
        return {"result": "error"}
    return {"result": get_art_by_masks(masks)}


@app.get("/get-mask-from-camera")
def get_mask_by_image_from_camera(
    camera_settings: Annotated[CameraSettings, Body()],
) -> dict[str, Any]:
    save_photo(
        get_photo_from_camera(camera_settings),
        PHOTO_NAME,
    )
    image = prepare_image(PHOTO_NAME)
    if image is None:
        return {"result": "error"}
    masks = fetch_masks_from_image(image)
    if masks is None:
        return {"result": "error"}
    return {"result": get_art_by_masks(masks)}


@app.get("/get-image-from-camera")
def get_image_from_camera(
    camera_settings: Annotated[CameraSettings, Body()],
) -> Response:
    return Response(
        get_photo_from_camera(camera_settings),
        media_type="image/jpg",
    )
