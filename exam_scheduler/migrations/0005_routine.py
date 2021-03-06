# Generated by Django 2.1.4 on 2021-01-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_scheduler', '0004_delete_routine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(default=None, max_length=20, primary_key=True, serialize=False, verbose_name='routine ID')),
                ('title', models.CharField(default=None, max_length=250, verbose_name='title')),
                ('batchAndSection', models.CharField(default=None, max_length=20)),
                ('courseName', models.CharField(default=None, max_length=20)),
                ('faculty', models.CharField(default=None, max_length=20, verbose_name='faculties')),
                ('room', models.CharField(default=None, max_length=20, verbose_name='room')),
                ('timeSlot', models.CharField(default=None, max_length=20, verbose_name='timeSlot')),
            ],
            options={
                'verbose_name': 'Routine',
                'verbose_name_plural': 'Routine',
                'db_table': '"tbl_routine"',
            },
        ),
    ]
