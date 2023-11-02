import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.utils import IntegrityError


class ShortenedLink(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=100, unique=True, blank=True)  # Allow it to be blank
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.short_link:  # If short_link is not provided
            while True:
                try:
                    self.short_link = str(uuid.uuid4())[:8]  # Generate a unique identifier
                    super().save(*args, **kwargs)
                except IntegrityError:  # Catch the exception if the short_link is not unique
                    continue
                break
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.short_link
    


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name