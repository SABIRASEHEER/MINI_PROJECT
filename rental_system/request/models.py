from django.db import models


class Request(models.Model):
    r_id = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=20)
    bid = models.IntegerField()
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'request'
