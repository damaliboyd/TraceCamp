# Generated by Django 2.1.4 on 2019-01-06 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.TextField()),
                ('type_of', models.TextField()),
                ('description', models.TextField()),
                ('location', models.IntegerField()),
                ('liked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='animalapp.Animal')),
            ],
        ),
    ]