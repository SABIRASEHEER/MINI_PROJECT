from django.db import models


class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=20)
    response = models.CharField(max_length=20)
    date = models.DateField()
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'
