from django.urls import path
from . import views
app_name = 'dashboard'


urlpatterns = [
    path('',views.Dashboard.as_view(), name='dashboard'),
    path('see/',views.Dashboard2, name='dashboard2'),
]