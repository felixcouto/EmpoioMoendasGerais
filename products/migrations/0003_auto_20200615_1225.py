# Generated by Django 3.0.7 on 2020-06-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200615_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='harmonizacao',
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='history',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='premios',
            field=models.TextField(max_length=120, null=True),
        ),
    ]
