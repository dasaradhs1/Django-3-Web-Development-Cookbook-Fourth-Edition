# Generated by Django 2.2.4 on 2019-09-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], null=True, verbose_name='Rating'),
        ),
    ]