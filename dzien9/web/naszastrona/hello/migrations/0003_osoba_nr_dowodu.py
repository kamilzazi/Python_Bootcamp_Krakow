# Generated by Django 3.0.2 on 2020-01-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='nr_dowodu',
            field=models.CharField(default='AAA000000', max_length=9),
            preserve_default=False,
        ),
    ]
