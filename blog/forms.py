import re
from django import forms
from django.core.validators import MinLengthValidator
from .models import Post, Comment


class PostForm(forms.Form):
    name = forms.CharField(validators=[MinLengthValidator(3)])
    desc = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        name = self.cleaned_data['name']
        desc = self.cleaned_data['desc']
        post = Post(name=name, desc=desc)
        if commit:
            post.save()
        return post

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['message']