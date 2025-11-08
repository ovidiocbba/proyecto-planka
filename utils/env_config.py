import os
from dotenv import load_dotenv

load_dotenv()

BASE_URI = os.getenv("BASE_URI")
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")