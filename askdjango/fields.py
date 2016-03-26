import os
from uuid import uuid4
from django.db import models


def random_name_upload_to(instance, filename):
    name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()
    return os.path.join(name[:2], name[2:] + ext)


class ImageField(models.ImageField):
    def __init__(self, **kwargs):
        kwargs.setdefault('upload_to', random_name_upload_to)
        super(ImageField, self).__init__(**kwargs)

class SquareImageField(ImageField):
    pass


class ThumbnailImageField(ImageField):
    pass

class FileField(models.FileField):
    def __init__(self, **kwargs):
        kwargs.setdefault('upload_to', random_name_upload_to)
        super(FileField, self).__init__(**kwargs)
