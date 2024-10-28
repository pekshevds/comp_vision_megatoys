from typing import Any
import face_recognition
import pickle
import cv2
from settings import DATA_URL


def prepare_image(image_name: str) -> Any:
    return cv2.imread(image_name)


def fetch_faces_from_image(image) -> list[Any] | None:
    try:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return face_recognition.face_encodings(rgb)
    except cv2.error:
        return None


def get_name_by_faces(faces) -> str:
    unknown = "Unknown"
    data = pickle.loads(open(DATA_URL, "rb").read())
    names = []
    for face in faces:
        matches = face_recognition.compare_faces(data["faces"], face)
        name = unknown
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts: dict[str, int] = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
            names.append(name)
    return names[0] if names else unknown
