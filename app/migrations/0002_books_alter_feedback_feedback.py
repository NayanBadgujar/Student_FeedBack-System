# Generated by Django 5.0 on 2024-02-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('author_name', models.TextField(max_length=20)),
                ('Price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(max_length=1500),
        ),
    ]
