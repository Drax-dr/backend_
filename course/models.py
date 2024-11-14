from django.db import models
from users.models import Student
from assignments.models import Assignment
import uuid

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=10,default=str(uuid.uuid4())[:8])
    assignments = models.ManyToManyField(Assignment, related_name='courses')
    students_enrolled = models.ManyToManyField(Student, related_name='courses')
    # course_type = models.CharField(max_length=10, choices=COURSE_TYPE_CHOICES, default='online')
    course_duration = models.PositiveIntegerField(help_text="Duration of the course in weeks")

    def __str__(self):
        return f"Course {self.id}"

    def total_students_enrolled(self):
        return self.students_enrolled.count()
