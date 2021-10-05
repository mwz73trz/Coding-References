from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Subject(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.title}"

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    notes = models.CharField(max_length=256)
    link = models.URLField(max_length=250)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return f"{self.id}, {self.name}, {self.description}, {self.notes}, {self.link}, {self.date_created}"


