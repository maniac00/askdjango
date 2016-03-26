import re
from django.core.files import File
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from askdjango.fields import ImageField
from askdjango.models import SquareModel
from askdjango.utils import square_image


def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    validator_fn = RegexValidator(r'^01[016789]\d{7,8}$', message='휴대폰 번호를 입력해주세요.')
    return validator_fn(number)

class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(phone_validator)

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    phone = PhoneField()

class Jjal(models.Model):
    name = models.CharField(max_length=100)
    image = ImageField()
    desc = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(SquareModel):
    square_size = 300
    image_field_name = 'photo'

    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    desc = models.TextField()
    photo = ImageField()
    tags = models.ManyToManyField('Tag', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

pre_save.connect(Post.on_pre_save, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True) # db_index=True
