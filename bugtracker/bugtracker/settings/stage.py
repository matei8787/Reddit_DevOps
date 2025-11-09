from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "bugtracker_prod"),
        "USER": os.getenv("DB_USER", "bugtracker_user"),
        "PASSWORD": os.getenv("DB_PASS", "secure_password"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

SECURE_SSL_REDIRECT = False
