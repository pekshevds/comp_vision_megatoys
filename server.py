# import os
from fastapi import FastAPI, UploadFile, File
from settings import UPLOAD_FOLDER
from services import save_file
from services.lib import prepare_image, fetch_faces_from_image, get_name_by_faces


app = FastAPI()


@app.post("/get-mask")
async def get_face_by_image(file: UploadFile = File(...)):
    # image_name = os.path.join(UPLOAD_FOLDER, str(file.filename))
    filename = UPLOAD_FOLDER / str(file.filename)
    save_file(file, str(filename))
    image = prepare_image(filename)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}
