# Generated by Django 2.0.3 on 2020-06-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaoyu', '0003_auto_20200620_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfoNew',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
