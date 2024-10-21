# Generated by Django 4.2.16 on 2024-10-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'такой маршрут уже существует'}, max_length=100, unique=True, verbose_name='Название маршрута')),
                ('slug', models.SlugField(blank=True, max_length=110, null=True, unique=True, verbose_name='URL')),
                ('base_city', models.CharField(max_length=50, verbose_name='Базовый город')),
                ('city_desc', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание горда')),
                ('route_desc', models.TextField(blank=True, max_length=7000, null=True, verbose_name='Описание маршрута')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка при наведении')),
                ('image_route1', models.ImageField(default='100.jpeg', upload_to='route_images')),
                ('image_route2', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_route3', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_route4', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_route5', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_route6', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_city1', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_city2', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_city3', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
                ('image_city4', models.ImageField(blank=True, default='100.jpeg', null=True, upload_to='route_images')),
            ],
            options={
                'verbose_name': 'Маршруты',
                'verbose_name_plural': 'Маршруты',
                'db_table': 'routes',
                'ordering': ['id'],
            },
        ),
    ]
