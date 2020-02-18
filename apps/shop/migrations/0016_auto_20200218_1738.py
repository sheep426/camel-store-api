# Generated by Django 2.2.9 on 2020-02-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200119_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='delivery_divide',
            field=models.CharField(choices=[('unlimit', '不限制'), ('radius', '半径划分'), ('geometry', '地图标注')], default='unlimit', max_length=20, verbose_name='配送范围划分方式'),
        ),
    ]