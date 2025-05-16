from django.urls import path
from .views import (
    AdListView, AdDetailView, AdCreateView, ResponseCreateView,
    ResponseListView, accept_response, reject_response, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', AdListView.as_view(), name='ad_list'),
    path('ads/', AdListView.as_view(), name='ad_list'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('ad/create/', AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:ad_id>/response/', ResponseCreateView.as_view(), name='response_create'),
    path('responses/', ResponseListView.as_view(), name='response_list'),
    path('responses/accept/<int:pk>/', accept_response, name='accept_response'),
    path('responses/reject/<int:pk>/', reject_response, name='reject_response'),
]