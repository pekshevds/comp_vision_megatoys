import sys
from utils.cv import prepare_image, fetch_masks_from_image, get_art_by_masks


def get_image_name():
    image_name = ""
    if len(sys.argv) >= 2:
        image_name = sys.argv[1]
    return image_name


def main():
    image_name = get_image_name()
    image = prepare_image(image_name)
    masks = fetch_masks_from_image(image)
    if masks:
        print(f"the mask in {image_name} belongs to {get_art_by_masks(masks)}")
    print("there is no faces")


if __name__ == "__main__":
    main()
