# Generated by Django 3.2.1 on 2022-07-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=150)),
                ('img', models.ImageField(default='', upload_to='food_items/')),
            ],
        ),
    ]
