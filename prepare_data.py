from imutils import paths
import face_recognition
import pickle
import cv2
import os


def get_images():
    return list(paths.list_images("Images"))


def get_people_name_from_path(image_path: str):
    return image_path.split(os.path.sep)[-2]


def get_encoding(image_path: str):
    rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    return face_recognition.face_encodings(rgb, boxes)


def main():
    knownEncodings = []
    knownNames = []
    for i, imagePath in enumerate(get_images()):
        name = get_people_name_from_path(imagePath)
        encodings = get_encoding(imagePath)
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
    data = {"encodings": knownEncodings, "names": knownNames}
    with open("face_enc", "wb") as f:
        f.write(pickle.dumps(data))


if __name__ == "__main__":
    main()
