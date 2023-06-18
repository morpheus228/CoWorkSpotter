from django.urls import path

from places.views import PlaceAddView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('places/add', PlaceAddView.as_view(), name='add_place'),
]

