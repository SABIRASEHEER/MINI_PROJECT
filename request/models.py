from django.db import models
from bike.models import Bike
from  user.models import User

class Request(models.Model):
    r_id = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=20)
    # b_id = models.IntegerField()
    b=models.ForeignKey(Bike, to_field='b_id', on_delete=models.CASCADE)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User, to_field='u_id', on_delete=models.CASCADE)
    time = models.TimeField()
    document = models.CharField(max_length=200)
    # bikename = models.CharField(max_length=34)

    class Meta:
        managed = False
        db_table = 'request'


