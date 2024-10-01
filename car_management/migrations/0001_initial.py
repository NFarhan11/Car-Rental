# Generated by Django 5.1 on 2024-09-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('rental_price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
        ),
    ]
