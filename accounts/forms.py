from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email


class SignupForm2(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3 + 4 * 2 = ?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 11:
            raise forms.ValidationError('땡~!!!')
        return answer