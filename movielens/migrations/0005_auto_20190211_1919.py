# Generated by Django 2.1.5 on 2019-02-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielens', '0004_user_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='filename',
            field=models.FilePathField(path='/home/ec2-user/environment/personalens/static/img'),
        ),
    ]
