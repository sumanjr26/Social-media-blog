from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SocialMedia(models.Model):
    USERNAME=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    photo=models.ImageField()
    users=models.IntegerField()
    content=models.CharField(max_length=100)
    strategies=models.CharField(max_length=100)
    reach=models.CharField(max_length=100)
    revenuegenerated=models.IntegerField()
    downside=models.CharField(max_length=100)

    def __str__(self):
        return self.name