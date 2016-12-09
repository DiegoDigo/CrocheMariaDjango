from django.conf import settings
from django.db import models


class ClienteModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)