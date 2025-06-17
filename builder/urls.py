from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_exe, name='home'),         # ✅ this name is used in {% url 'home' %}
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-builds/', views.my_builds, name='my_builds'),
]
