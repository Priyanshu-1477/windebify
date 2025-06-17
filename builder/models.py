# builder/models.py
from django.db import models

class Build(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exe_file = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.status}'

# Create your models here.
