from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from settings import UPLOAD_FOLDER, templates
from services import save_file
from services.lib import prepare_image, fetch_faces_from_image, get_name_by_faces


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "index"},
    )


@app.post("/get-mask")
async def get_face_by_image(file: UploadFile = File(...)):
    filename = UPLOAD_FOLDER / str(file.filename)
    save_file(file, str(filename))
    image = prepare_image(filename)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}
