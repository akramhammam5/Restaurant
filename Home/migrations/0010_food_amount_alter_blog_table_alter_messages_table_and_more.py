# Generated by Django 4.2.3 on 2023-08-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_rename_news_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Amount',
            field=models.IntegerField(blank=True, default=25),
        ),
        migrations.AlterModelTable(
            name='blog',
            table='Blogs',
        ),
        migrations.AlterModelTable(
            name='messages',
            table='Messages',
        ),
        migrations.AlterModelTable(
            name='new',
            table='News',
        ),
    ]
