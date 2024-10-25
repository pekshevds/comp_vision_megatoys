import os
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from lib import prepare_image, fetch_faces_from_image, get_name_by_faces


def save_file(file: InMemoryUploadedFile) -> str:
    image_name = os.path.join(settings.MEDIA_ROOT, "image.JPG")
    content = file.file.read()
    with open(image_name, "wb") as f:
        f.write(content)
    return image_name


def get_faces(image_name) -> str:
    error = "error"
    image = prepare_image(image_name)
    if image is None:
        return error
    faces = fetch_faces_from_image(image)
    if faces is None:
        return error
    return get_name_by_faces(faces)
