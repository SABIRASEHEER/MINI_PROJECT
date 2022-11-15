# Generated by Django 3.2.14 on 2022-11-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField()),
                ('amount', models.CharField(max_length=20)),
                ('b_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
