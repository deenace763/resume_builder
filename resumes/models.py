from django.contrib.auth.models import User
from django.db import models

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)

    education = models.TextField(blank=True, help_text="List your education")
    experience = models.TextField(blank=True, help_text="Work experience")
    skills = models.TextField(blank=True)
    projects = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.user.username}"
