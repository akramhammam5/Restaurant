# Generated by Django 3.2.20 on 2023-08-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
