from django.urls import path
from .views import (
            ThreadListView,
            ThreadDetailView,
            ThreadCreateView,
            ThreadUpdateView,
            ThreadDeleteView
)
from . import views

urlpatterns = [
    path('', ThreadListView.as_view(), name='main-home'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/new/', ThreadCreateView.as_view(), name='thread-create'),
    path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
]
