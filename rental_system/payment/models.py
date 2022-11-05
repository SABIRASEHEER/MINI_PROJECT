from django.db import models


class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    amount = models.CharField(max_length=20)
    b_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'payment'



