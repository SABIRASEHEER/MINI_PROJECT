from django.db import models
from user.models import User


class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=20)
    response = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    replytime = models.CharField(max_length=20)
    replydate = models.CharField(max_length=20)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User, to_field='u_id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'complaint'


