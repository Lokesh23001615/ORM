# Generated by Django 5.0.2 on 2024-02-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=30)),
                ('bookprice', models.IntegerField()),
                ('author', models.CharField(max_length=30)),
                ('qty', models.IntegerField()),
            ],
        ),
    ]