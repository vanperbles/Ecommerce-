from django.urls import path
from . import views
app_name = 'myAuth'

urlpatterns = [
    # path('', views.Index, name = "index"),
    path('login_page/', views.login_page, name='login_page'),
    path('login_api/', views.login_api, name='login_api'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('register/', views.register, name='register'),
    path('register_api/', views.register_api, name='register-api'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]