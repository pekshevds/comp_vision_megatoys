from typing import Any
import face_recognition
import pickle
import cv2
from settings import DATA_URL


class ImreadException(Exception):
    pass


def prepare_image(image_name: str) -> Any | None:
    try:
        return cv2.imread(image_name)
    except ImreadException:
        return None


def fetch_masks_from_image(prepare_image) -> list[Any] | None:
    try:
        rgb = cv2.cvtColor(prepare_image, cv2.COLOR_BGR2RGB)
        return face_recognition.face_encodings(rgb)
    except cv2.error:
        return None


def get_art_by_masks(masks) -> str:
    unknown = "Unknown"
    data = pickle.loads(open(DATA_URL, "rb").read())
    arts = []
    for mask in masks:
        matches = face_recognition.compare_faces(data["masks"], mask)
        art = unknown
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts: dict[str, int] = {}
            for i in matchedIdxs:
                name = data["arts"][i]
                counts[name] = counts.get(art, 0) + 1
                name = max(counts, key=counts.get)
            arts.append(name)
    return arts[0] if arts else unknown
