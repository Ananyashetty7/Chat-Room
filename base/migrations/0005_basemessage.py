# Generated by Django 5.1.3 on 2024-12-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_message_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
