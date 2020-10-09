# Generated by Django 3.1.2 on 2020-10-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title text on index')),
                ('hallow_text', models.TextField(verbose_name='hallow text on index')),
                ('description', models.TextField(verbose_name='description about bamazone')),
            ],
        ),
    ]
