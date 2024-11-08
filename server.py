from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, Response
from settings import templates, CAMERA_SETTINGS, PHOTO_NAME
from services import save_file, save_photo
from services.cv import prepare_image, fetch_faces_from_image, get_name_by_faces
from services.camera import get_photo_from_camera


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "index"},
    )


@app.get("/get-mask")
def get_face_by_image_from_camera():
    save_photo(
        get_photo_from_camera(
            CAMERA_SETTINGS["camera_ip"],
            CAMERA_SETTINGS["username"],
            CAMERA_SETTINGS["password"],
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


@app.get("/get-image")
def get_image_from_camera():
    return Response(
        get_photo_from_camera(
            CAMERA_SETTINGS["camera_ip"],
            CAMERA_SETTINGS["username"],
            CAMERA_SETTINGS["password"],
        ),
        media_type="image/jpg",
    )


@app.post("/get-mask")
def get_face_by_image_from_file(file: UploadFile = File(...)):
    save_file(file, PHOTO_NAME)
    image = prepare_image(PHOTO_NAME)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}
