# Generated by Django 4.1.3 on 2022-11-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0014_jobtype_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='partsprice',
            name='details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
