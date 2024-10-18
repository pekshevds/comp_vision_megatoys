import sys
import face_recognition
import pickle
import cv2


def prepare_image(image_name):
    return cv2.imread(image_name)


def fetch_faces_from_image(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return face_recognition.face_encodings(rgb)


def get_name_by_faces(faces):
    unknown = "Unknown"
    data = pickle.loads(open("face_enc", "rb").read())
    names = []
    for face in faces:
        matches = face_recognition.compare_faces(data["encodings"], face)
        name = unknown
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)

            names.append(name)
    return names[0] if names else unknown


def main():
    image_name = ""
    if len(sys.argv) >= 2:
        image_name = sys.argv[1]
    image = prepare_image(image_name)
    faces = fetch_faces_from_image(image)
    print(f"the face in {image_name} belongs to {get_name_by_faces(faces)}")


if __name__ == "__main__":
    main()
