from django.urls import path

from .views import (
    refugeeCreateView
)

app_name = "refugees"
urlpatterns = [
    path("refugee_create/", view=refugeeCreateView.as_view(), name="refugee_create"),
]
