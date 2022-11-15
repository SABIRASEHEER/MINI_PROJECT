from django.db import models
from  bike.models import Bike
from user.models import User


class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User, to_field='u_id', on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)
    # b_id = models.IntegerField()
    b=models.ForeignKey(Bike, to_field='b_id', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'payment'



