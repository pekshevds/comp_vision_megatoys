import os
import uvicorn
from fastapi import FastAPI, UploadFile, File
from lib import prepare_image, fetch_faces_from_image, get_name_by_faces

UPLOAD_FOLDER = "upload"
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}
app = FastAPI()


@app.post("/get-mask")
async def get_face_by_image(file: UploadFile = File(...)):
    image_name = os.path.join(UPLOAD_FOLDER, str(file.filename))
    content = file.file.read()
    with open(image_name, "wb") as f:
        f.write(content)

    image = prepare_image(image_name)
    if image is None:
        return {"result": "error"}
    faces = fetch_faces_from_image(image)
    if faces is None:
        return {"result": "error"}
    return {"result": get_name_by_faces(faces)}


# if __name__ == "__main__":
#     uvicorn.run(app=app, host="0.0.0.0", port=8081)
