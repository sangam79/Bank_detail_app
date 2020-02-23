from django.urls import path
from restapi.views import IndianbankAPIView, IndianbankDetails


urlpatterns = [
    path('', IndianbankAPIView.as_view()),
    path('details/<int:id>/', IndianbankDetails.as_view()),
]    