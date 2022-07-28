# Generated by Django 4.0.6 on 2022-07-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('emp_id', models.CharField(max_length=7)),
                ('mobile', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
