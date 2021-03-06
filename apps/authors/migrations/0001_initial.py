# Generated by Django 3.1.2 on 2020-10-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name="Author's name")),
                ('last_name', models.CharField(max_length=64, verbose_name="Author's last name")),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
