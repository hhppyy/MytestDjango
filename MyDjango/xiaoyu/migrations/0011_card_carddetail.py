# Generated by Django 2.0.3 on 2020-06-28 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xiaoyu', '0010_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=30, verbose_name='银行卡号')),
                ('card_user', models.CharField(max_length=30, verbose_name='持卡人')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '银行卡',
            },
        ),
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='持卡人手机号')),
                ('mail', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='邮箱')),
                ('city', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='城市')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地址')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='xiaoyu.Card', verbose_name='银行卡号')),
            ],
            options={
                'verbose_name_plural': '银行卡详情',
            },
        ),
    ]
