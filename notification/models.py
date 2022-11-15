from django.db import models


class Notification(models.Model):
    n_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=20)
    date = models.DateField()
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'notification'
