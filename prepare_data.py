from imutils import paths
import face_recognition
import pickle
import cv2
import os


def get_images():
    return list(paths.list_images("Images"))


def get_people_name_from_path(image_path: str):
    return image_path.split(os.path.sep)[-2]


def extract_faces(image_path: str):
    rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    return face_recognition.face_encodings(rgb, boxes)


def main():
    known_faces = []
    known_names = []
    for i, imagePath in enumerate(get_images()):
        name = get_people_name_from_path(imagePath)
        faces = extract_faces(imagePath)
        for face in faces:
            known_faces.append(face)
            known_names.append(name)
    data = {"faces": known_faces, "names": known_names}
    with open("face_enc", "wb") as f:
        f.write(pickle.dumps(data))


if __name__ == "__main__":
    main()
