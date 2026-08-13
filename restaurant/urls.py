from django.urls import path
from .views import (
    MenuListCreateView,
    MenuDetailView,
    BookingListCreateView,
    BookingDetailView,
)


urlpatterns = [
    path('menu/', MenuListCreateView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),

    path('booking/', BookingListCreateView.as_view(), name='booking-list'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]