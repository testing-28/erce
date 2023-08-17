# Generated by Django 4.2.2 on 2023-08-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devblogs', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
