from django.urls import path
from .views import HomeView, MenuList, MenuItem, BookingList, BookingItem

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuList.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuItem.as_view(), name='menu-item'),
    path('booking/', BookingList.as_view(), name='booking-list'),
    path('booking/<int:pk>/', BookingItem.as_view(), name='booking-item'),
]