from django.urls import path
from .views import ShortenedLinkListCreateView

urlpatterns = [
    path('create_short_link/', ShortenedLinkListCreateView.as_view(), name='create_short_link'),
   
]
