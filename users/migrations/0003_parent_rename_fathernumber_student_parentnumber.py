# Generated by Django 5.1.2 on 2024-11-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_parents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('studentID', models.CharField(error_messages={'unique': 'A user with that ID already exists.'}, max_length=10, unique=True)),
                ('phoneNumber', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fatherNumber',
            new_name='ParentNumber',
        ),
    ]