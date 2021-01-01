# Generated by Django 3.0.8 on 2020-12-31 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Start', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startmodel',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='startModel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='startmodel',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
