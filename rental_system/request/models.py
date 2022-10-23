from django.db import models


class Request(models.Model):
    r_id = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=20)
    b_id = models.IntegerField()
    u_id = models.IntegerField()
    time = models.TimeField()
    document = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'request'


