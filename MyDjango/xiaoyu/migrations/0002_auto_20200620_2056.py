# Generated by Django 2.0.3 on 2020-06-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaoyu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
