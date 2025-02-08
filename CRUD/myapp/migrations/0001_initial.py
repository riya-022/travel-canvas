# Generated by Django 5.1.5 on 2025-02-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('password', models.CharField(max_length=8)),
                ('address', models.TextField()),
                ('profilepicture', models.ImageField(upload_to='photos')),
                ('gender', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
