# Generated by Django 3.2 on 2021-05-01 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0002_auto_20210428_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('address', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
