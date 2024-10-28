from fastapi import UploadFile


def save_file(file: UploadFile, filename: str) -> None:
    content = file.file.read()
    with open(filename, "wb") as f:
        f.write(content)
