# Generated by Django 4.1.7 on 2023-07-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedias',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('users', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('strategies', models.CharField(max_length=100)),
                ('reach', models.CharField(max_length=100)),
                ('revenuegenerated', models.IntegerField()),
                ('downside', models.CharField(max_length=100)),
            ],
        ),
    ]
