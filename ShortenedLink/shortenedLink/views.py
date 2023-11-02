from rest_framework import generics
from rest_framework.response import Response
from .serializers import ShortenedLinkSerializer
from .models import ShortenedLink
from rest_framework.permissions import IsAuthenticated
import uuid

class ShortenedLinkListCreateView(generics.ListCreateAPIView):
    serializer_class = ShortenedLinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShortenedLink.objects.filter(created_by=user)

    def perform_create(self, serializer):
        user = self.request.user
        original_link = serializer.validated_data['original_link']
        short_link = generate_short_link(original_link)
        serializer.save(short_link=short_link, created_by=user)

def generate_short_link(original_link):
    unique_id = str(uuid.uuid4())[:8]  # Extract the first 8 characters of the UUID
    return unique_id

