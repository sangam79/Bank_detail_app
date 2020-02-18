from django.urls import path

from . import views
from bankapp.views import HomeView, DisplayView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('display/', DisplayView.as_view(), name='display'),
]    