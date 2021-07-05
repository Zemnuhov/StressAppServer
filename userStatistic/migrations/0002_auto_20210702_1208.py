# Generated by Django 3.2.4 on 2021-07-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userStatistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default='123', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statistic',
            name='dateTime',
            field=models.IntegerField(),
        ),
    ]