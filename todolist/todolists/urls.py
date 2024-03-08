from django.urls import path

from todolists import views

urlpatterns = [
    path('', views.top, name="top"),
]