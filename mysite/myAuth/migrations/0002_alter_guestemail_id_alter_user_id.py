# Generated by Django 4.2.6 on 2023-10-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]