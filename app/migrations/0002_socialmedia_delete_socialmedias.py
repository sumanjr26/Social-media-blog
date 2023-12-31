# Generated by Django 4.1.7 on 2023-07-08 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('users', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('strategies', models.CharField(max_length=100)),
                ('reach', models.CharField(max_length=100)),
                ('revenuegenerated', models.IntegerField()),
                ('downside', models.CharField(max_length=100)),
                ('USERNAME', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='SocialMedias',
        ),
    ]
