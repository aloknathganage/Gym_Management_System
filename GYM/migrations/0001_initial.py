# Generated by Django 3.2.9 on 2023-03-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(default='', max_length=10)),
                ('plan', models.CharField(max_length=50)),
                ('joindate', models.DateField(max_length=40)),
                ('expiredate', models.DateField(max_length=40)),
                ('initialamount', models.CharField(max_length=10)),
            ],
        ),
    ]
