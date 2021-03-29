# Generated by Django 2.1.4 on 2021-02-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_scheduler', '0005_routine'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='crs_credit',
            field=models.FloatField(blank=True, null=True, verbose_name='credit'),
        ),
        migrations.AddField(
            model_name='routine',
            name='day',
            field=models.CharField(blank=True, default=None, max_length=12, null=True),
        ),
    ]