# Generated by Django 2.1.2 on 2019-04-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.FloatField(default=0.0)),
            ],
        ),
    ]