# Generated by Django 2.2.1 on 2019-05-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20190514_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carset',
            name='acceleration',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='carset',
            name='displacement',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='carset',
            name='horsepower',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='carset',
            name='mpg',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='carset',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]