# Generated by Django 4.2 on 2023-06-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='fields',
            field=models.ManyToManyField(to='records.field'),
        ),
    ]