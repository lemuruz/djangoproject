# Generated by Django 5.1.3 on 2024-12-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=50000)),
                ('Pub_Date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

