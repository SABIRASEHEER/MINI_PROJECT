from django.db import models
class Bike(models.Model):
    b_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    conditions = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    availability = models.CharField(max_length=20)
    image = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'bike'




