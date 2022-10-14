from django.db import models


class Payment(models.Model):
    p_id = models.IntegerField()
    u_id = models.IntegerField()
    amount = models.CharField(max_length=20)
    method = models.CharField(max_length=20)
    b_id = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'payment'
