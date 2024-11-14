from django.db import models
# from users.models import Student

from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class CompletedAssignment(models.Model):
    # ForeignKey to Student and Assignment models
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    completed_on = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('completed', 'Completed'), ('pending', 'Pending')],
        default='pending'
    )

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title} - {self.status}"


class Question(models.Model):
    assignment = models.ForeignKey(Assignment, related_name="questions", on_delete=models.CASCADE)
    question_text = models.TextField()
    marks = models.IntegerField(default=0)
    answer_type = models.CharField(max_length=50, choices=[('multiple_choice', 'Multiple Choice'), ('short_answer', 'Short Answer')], default='short_answer')

    def __str__(self):
        return f"Question: {self.question_text[:50]}..."

