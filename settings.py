from pathlib import Path
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "upload"
DATA_URL = BASE_DIR / "data/face_enc"
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}
