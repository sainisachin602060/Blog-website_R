# Generated by Django 4.1.3 on 2023-06-23 04:19

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0003_rename_email_contactquery_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=200)),
                ('Catogery', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('postedDate', models.DateField(default=datetime.date(2023, 6, 23))),
                ('good_name', models.CharField(max_length=200)),
            ],
        ),
    ]
