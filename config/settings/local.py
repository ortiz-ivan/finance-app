from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret")

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backend.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
