# Generated by Django 4.1.3 on 2022-11-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=55)),
                ('address', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=55)),
                ('age', models.DateField(default=1902)),
            ],
        ),
    ]
