from django.db import models
from user.models import CustomUser

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    favo_at = models.DateTimeField()
    is_delete = models.BooleanField(default=False)