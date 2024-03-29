# Generated by Django 4.2.8 on 2024-02-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partyupapi', '0007_alter_lfgpost_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.EmailField(default='email', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='joinDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
