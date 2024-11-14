from typing import Any
from pathlib import Path
from fastapi import UploadFile
from settings import UPLOAD_FOLDER


def save_file(file: UploadFile, filename: Path | str) -> None:
    save_photo(file.file.read(), UPLOAD_FOLDER / filename)


def save_photo(binary: Any, filename: Path | str) -> None:
    with open(filename, "wb") as f:
        f.write(binary)
