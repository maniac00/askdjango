from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name':'accounts/login.html', 'authentication_form': LoginForm})]