# Generated by Django 3.0 on 2019-12-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=None, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]