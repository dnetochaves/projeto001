from django.urls import path
from . import views

app_name = "apps.recipes"

urlpatterns = [
    path('', views.index, name="index"),
]