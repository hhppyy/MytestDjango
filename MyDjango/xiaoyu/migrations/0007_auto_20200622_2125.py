# Generated by Django 2.0.3 on 2020-06-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaoyu', '0006_auto_20200622_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfonew',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
