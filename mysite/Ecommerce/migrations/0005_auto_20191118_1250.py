# Generated by Django 2.2.7 on 2019-11-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0004_auto_20191118_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_Images'),
        ),
    ]
