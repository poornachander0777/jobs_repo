# Generated by Django 3.2.4 on 2021-12-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Husnabadjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=30)),
                ('JobName', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=30)),
                ('Experience', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('ContactNumber', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mumbaijobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=30)),
                ('JobName', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=30)),
                ('Experience', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('ContactNumber', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Punejobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=30)),
                ('JobName', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=30)),
                ('Experience', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('ContactNumber', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]
