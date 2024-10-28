import sys
from services.lib import prepare_image, fetch_faces_from_image, get_name_by_faces


def get_image_name():
    image_name = ""
    if len(sys.argv) >= 2:
        image_name = sys.argv[1]
    return image_name


def main():
    image_name = get_image_name()
    image = prepare_image(image_name)
    faces = fetch_faces_from_image(image)
    if faces:
        print(f"the face in {image_name} belongs to {get_name_by_faces(faces)}")
    print("there is no faces")


if __name__ == "__main__":
    main()
