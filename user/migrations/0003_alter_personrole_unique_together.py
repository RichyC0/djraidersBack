# Generated by Django 5.0.2 on 2024-09-07 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_person_is_active_person_is_staff_person_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personrole',
            unique_together={('person', 'role')},
        ),
    ]
