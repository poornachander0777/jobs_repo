# Generated by Django 3.2.4 on 2021-12-20 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0002_husnabadjobs_mumbaijobs_punejobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='husnabadjobs',
            name='ContactNumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='ContactNumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mumbaijobs',
            name='ContactNumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='punejobs',
            name='ContactNumber',
            field=models.CharField(max_length=30),
        ),
    ]
