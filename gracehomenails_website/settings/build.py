from .base import *


# Use the production static files backend when collecting static assets.
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"
