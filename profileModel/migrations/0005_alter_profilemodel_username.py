# Generated by Django 5.0.4 on 2024-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileModel', '0004_alter_profilemodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
