from django.db import models
from user.models import CustomUser

class Chat(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    detail = models.CharField(max_length=255,blank=True,null=True)
    link = models.CharField(max_length=255,blank=True,null=True)
    is_system = models.BooleanField(default=False)
<<<<<<< HEAD
    send_at = models.DateTimeField()
=======
    send_at = models.DateTimeField()
