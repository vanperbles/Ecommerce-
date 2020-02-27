from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [

    path('register', register, name="register"),
    path('login/', auth_views.LoginView(template_name='login.html'), name="login"),

]