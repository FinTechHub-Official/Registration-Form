# Generated by Django 4.2.3 on 2024-01-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_target_registration_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='link',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
