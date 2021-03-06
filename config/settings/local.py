from .base import *
from .base import env

ALLOWED_HOSTS = ["0.0.0.0"]

ADMINS = (
    ('vlad doster', 'mvdoster@gmail.com'),
)

MANAGERS = ADMINS

INSTALLED_APPS += ["debug_toolbar",
                   "django_extensions",
                   "crispy_forms", ]

# Crispy forms
# ------------------------------------------------------------------------------
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]
