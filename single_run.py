import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askdjango.settings')

import django
django.setup()

'''
from blog.models import Jjal

for jjal in Jjal.objects.all():
    print(jjal.name)
'''

import random
from blog.models import Post, Comment

for i in range(1000):
    post_id = random.randint(1, 100)
    try:
        post = Post.objects.get(pk=post_id)
        comment = Comment(post=post, message='message for post#{}'.format(post_id))
        comment.save()
    except Post.DoesNotExist:
        print('not found post#{}'.format(post_id))