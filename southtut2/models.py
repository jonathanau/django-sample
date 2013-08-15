from django.db import models

class User(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=60)
  name = models.TextField()
