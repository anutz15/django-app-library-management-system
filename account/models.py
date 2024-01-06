from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    # other fields
    roll_no = models.CharField(max_length=10, blank=True)
    branch = models.CharField(max_length=10, blank=True)

    otp = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.roll_no}"