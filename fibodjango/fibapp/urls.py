from django.urls import path
from .views import fibView

urlpatterns = [
    path('', fibView),
]
