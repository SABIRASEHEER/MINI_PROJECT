from django.db import models



class Staff(models.Model):
    s_id = models.AutoField(primary_key=True)
    staffname = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    salary_day = models.CharField(db_column='salary/day', max_length=20)  # Field renamed to remove unsuitable characters.
    day_present = models.CharField(db_column='day present', max_length=20)  # Field renamed to remove unsuitable characters.
    category = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'staff'

