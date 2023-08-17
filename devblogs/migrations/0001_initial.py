# Generated by Django 4.2.2 on 2023-08-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
