# Generated by Django 2.1.4 on 2020-02-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art_paintingxclientmood',
            name='art_paintingid',
        ),
        migrations.RemoveField(
            model_name='art_paintingxclientmood',
            name='clientmoodid',
        ),
        migrations.RemoveField(
            model_name='art_paintingxpaintcolor',
            name='art_paintingid',
        ),
        migrations.RemoveField(
            model_name='art_paintingxpaintcolor',
            name='paintcolorid',
        ),
        migrations.AddField(
            model_name='art_painting',
            name='clientmoods',
            field=models.ManyToManyField(to='trackart.clientmood'),
        ),
        migrations.AddField(
            model_name='art_painting',
            name='paintcolors',
            field=models.ManyToManyField(to='trackart.paintcolor'),
        ),
        migrations.DeleteModel(
            name='art_paintingXclientmood',
        ),
        migrations.DeleteModel(
            name='art_paintingXpaintcolor',
        ),
    ]
