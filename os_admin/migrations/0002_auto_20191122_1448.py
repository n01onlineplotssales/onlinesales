# Generated by Django 2.2.4 on 2019-11-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlogin',
            name='a_contact_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agent',
            name='ag_contact_no',
            field=models.BigIntegerField(),
        ),
    ]
