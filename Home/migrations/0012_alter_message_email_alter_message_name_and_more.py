# Generated by Django 4.2.3 on 2023-08-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_message_delete_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(null=True),
        ),
    ]