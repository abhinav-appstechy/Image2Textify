# Generated by Django 5.0.4 on 2024-05-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OcrModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
