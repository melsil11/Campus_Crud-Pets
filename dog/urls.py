from django.urls import path
from .views.dog_views import DogsView, DogDetailView
from .views.owner_views import OwnersView, OwnerDetailView 

urlpatterns = [
    path('dogs/', DogsView.as_view(), name='dogs'),
    path('dogs/<int:pk>/', DogDetailView.as_view(), name='dog'),
    path('owners/', OwnersView.as_view(), name='owners'),
    path('owners/<int:pk>/', OwnerDetailView.as_view(), name='owner'),
]