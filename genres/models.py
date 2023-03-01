from django.db import models
from uuid import uuid4


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=127)
