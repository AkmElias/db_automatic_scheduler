# Generated by Django 2.1.4 on 2020-12-12 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_scheduler', '0006_auto_20201212_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='roomCode',
        ),
        migrations.DeleteModel(
            name='Routine',
        ),
    ]