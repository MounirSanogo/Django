from django.urls import path
from .views import CoursCreateView, CoursDeleteView, MessageListView, MessageCreateView

urlpatterns = [
    path('cours/create/', CoursCreateView.as_view(), name='cours-create'),
    path('cours/delete/<int:pk>/', CoursDeleteView.as_view(), name='cours-delete'),
    path('cours/<int:cours_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('cours/<int:cours_id>/messages/new/', MessageCreateView.as_view(), name='message-create'),
]
