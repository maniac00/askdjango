from django.db import models

class SquareModel(models.Model):
    square_size = None
    image_field_name = 'image'

    class Meta:
        abstract = True

    @classmethod
    def on_pre_save(cls, sender, **kwargs):
        instance = kwargs['instance']
        image_field = getattr(instance, cls.image_field_name)

        if image_field and cls.square_size:
            if image_field.width > cls.square_size or image_field.height > cls.square_size:
                sqaured_f = square_image(image_field.file, cls.square_size)
                image_field.save(image_field.name, File(sqaured_f))