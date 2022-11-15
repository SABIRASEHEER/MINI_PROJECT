from django.db import models


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    uaddress = models.CharField(max_length=20)
    aadharnum = models.CharField(max_length=20)
    licensenum = models.CharField(max_length=20)
    pancardno = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=65)
    status = models.CharField(max_length=22)

    class Meta:
        managed = False
        db_table = 'user'
