# Generated by Django 2.0.1 on 2018-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdriveApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileUploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
                ('file_uploader', models.CharField(max_length=200)),
            ],
        ),
    ]
