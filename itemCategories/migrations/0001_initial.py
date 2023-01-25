# Generated by Django 4.1.5 on 2023-01-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('group', models.CharField(max_length=250)),
                ('sub_group', models.CharField(max_length=250)),
                ('brand_name', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
            ],
        ),
    ]
