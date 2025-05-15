from django.urls import path
from genba_manager_app import views

urlpatterns = [
    path("", views.home, name="home"),
]
