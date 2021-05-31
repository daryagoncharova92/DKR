from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    create = models.DateField(auto_now_add=True)