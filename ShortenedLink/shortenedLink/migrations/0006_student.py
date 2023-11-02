# Generated by Django 4.1.5 on 2023-11-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenedLink', '0005_delete_linkhit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]