from django.urls import path
from .views import ShortenedLinkListCreateView , StudentListCreateView

urlpatterns = [
    path('create_short_link/', ShortenedLinkListCreateView.as_view(), name='create_short_link'),
   path('addStudent/', StudentListCreateView.as_view(), name='Add Student'),
]
