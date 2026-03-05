from .base import *  # noqa: F401,F403

DJANGO_ENV = "staging"
DEBUG = False

DATABASE_URL = config("DATABASE_URL", default="")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is required for staging environment")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

CORS_ALLOW_ALL_ORIGINS = False

if "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.remove("debug_toolbar")
if "django_extensions" in INSTALLED_APPS:
    INSTALLED_APPS.remove("django_extensions")
if "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
    MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
