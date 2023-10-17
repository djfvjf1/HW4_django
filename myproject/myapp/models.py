from django.contrib.auth.models import User
from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    description = models.TextField()
    priority_choices = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)
    resolved_problems = [
        ('resolved', 'решено'),
        ('not resolved', 'не решено'),
    ]
    resolved = models.CharField(max_length=20, choices=resolved_problems, default='none')
    created_at = models.DateTimeField(auto_now_add=True)  # Поле даты создания

    def __str__(self):
        return self.name