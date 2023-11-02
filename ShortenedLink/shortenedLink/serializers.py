from rest_framework import serializers
from .models import ShortenedLink , Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedLink
        fields = '__all__'
