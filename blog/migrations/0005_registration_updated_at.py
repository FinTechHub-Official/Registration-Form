# Generated by Django 4.2.3 on 2023-09-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_registration_kurs'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]