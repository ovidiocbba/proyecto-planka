import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BASE_URI = os.getenv("BASE_URI")
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")


if not USER_EMAIL or not USER_PASSWORD:
    raise RuntimeError(" Error: No se cargaron las variables desde .env")
