from django.db import models
# Create your models here.

from django.contrib.auth import get_user_model
class PNR(models.Model):
    User=get_user_model()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pnr=models.IntegerField(default=0)
    train_number=models.IntegerField(default=0)
    source_station=models.CharField(max_length=100,default='')
    destination_station=models.CharField(max_length=100 , default='')
    distance=models.IntegerField(default=0)
    
    def __str__(self):
        return 'pnr details'

    def user_info(self):
        return f"User: {self.user.username}"
