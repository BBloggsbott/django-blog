# Generated by Django 2.1.2 on 2018-11-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181103_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
