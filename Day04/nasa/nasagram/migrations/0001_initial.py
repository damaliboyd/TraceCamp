# Generated by Django 2.1.4 on 2019-01-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nasagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.TextField()),
                ('heart', models.BooleanField()),
                ('url', models.URLField()),
                ('date', models.DateField()),
            ],
        ),
    ]
