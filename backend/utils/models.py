import uuid
from django.db import models

# Create your models here.
class UUIDModel(models.Model):
    """
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """

    id = models.UUIDField(
        primary_key=True, editable=False, auto_created=True, default=uuid.uuid4
    )

    class Meta:
        abstract = True
