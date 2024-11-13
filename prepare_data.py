from typing import Any
from imutils import paths
import face_recognition
import pickle
import cv2
import os
from settings import DATA_URL


def get_images() -> list[Any]:
    return list(paths.list_images("Images"))


def get_mask_art_from_path(image_path: str) -> str:
    return image_path.split(os.path.sep)[-2]


def extract_masks(image_path: str) -> list[Any] | None:
    try:
        rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        return face_recognition.face_encodings(rgb, boxes)
    except cv2.error:
        return None


def main():
    known_masks = []
    known_arts = []
    for _, image_path in enumerate(get_images()):
        art = get_mask_art_from_path(image_path)
        masks = extract_masks(image_path)
        for mask in masks:
            known_masks.append(mask)
            known_arts.append(art)
    data = {"masks": known_masks, "arts": known_arts}
    with open(DATA_URL, "wb") as f:
        f.write(pickle.dumps(data))


if __name__ == "__main__":
    main()
