from .base import *
import os
import dj_database_url

DJANGO_ENV = "production"
DEBUG = False

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
    )
}

ALLOWED_HOSTS = [".railway.app"]

CSRF_TRUSTED_ORIGINS = [
    f"https://{os.getenv('RAILWAY_PUBLIC_DOMAIN')}"
] if os.getenv("RAILWAY_PUBLIC_DOMAIN") else []

# Proxy settings (Railway)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Desativar redirect forçado (Railway já usa HTTPS)
SECURE_SSL_REDIRECT = False

# HSTS (opcional)
SECURE_HSTS_SECONDS = 0

# Remover ferramentas de dev
if "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.remove("debug_toolbar")

if "django_extensions" in INSTALLED_APPS:
    INSTALLED_APPS.remove("django_extensions")

if "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
    MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")