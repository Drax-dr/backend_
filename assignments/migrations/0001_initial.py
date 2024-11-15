# Generated by Django 5.1.2 on 2024-11-06 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CompletedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=10)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('marks', models.IntegerField(default=0)),
                ('answer_type', models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('short_answer', 'Short Answer')], default='short_answer', max_length=50)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='assignments.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('studentID', models.CharField(max_length=10, unique=True)),
                ('phoneNumber', models.CharField(max_length=10, unique=True)),
                ('fatherNumber', models.CharField(max_length=10)),
                ('profilePic', models.ImageField(upload_to='assets/images')),
                ('grade', models.IntegerField(default=8)),
                ('assignments_completed', models.ManyToManyField(related_name='students', through='assignments.CompletedAssignment', to='assignments.assignment')),
            ],
        ),
        migrations.AddField(
            model_name='completedassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.student'),
        ),
    ]
