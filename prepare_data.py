from typing import Any
from imutils import paths
import face_recognition
import pickle
import cv2
import os
from settings import DATA_URL


def get_images() -> list[Any]:
    return list(paths.list_images("Images"))


def get_mask_name_from_path(image_path: str) -> str:
    return image_path.split(os.path.sep)[-2]


def extract_faces(image_path: str) -> list[Any] | None:
    try:
        rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        return face_recognition.face_encodings(rgb, boxes)
    except cv2.error:
        return None


def main():
    known_faces = []
    known_names = []
    for i, image_path in enumerate(get_images()):
        name = get_mask_name_from_path(image_path)
        faces = extract_faces(image_path)
        for face in faces:
            known_faces.append(face)
            known_names.append(name)
    data = {"faces": known_faces, "names": known_names}
    with open(DATA_URL, "wb") as f:
        f.write(pickle.dumps(data))


if __name__ == "__main__":
    main()
