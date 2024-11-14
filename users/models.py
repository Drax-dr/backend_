from django.db import models
from django.db.models.enums import Choices
from django.contrib.auth.hashers import make_password
from django.forms.widgets import PasswordInput
from assignments.models import Assignment, CompletedAssignment
from django.apps import apps
import uuid

GRADE_CHOICCES = [
    (
        8, 'EIGHT',
        9, 'NINGHT',
        10, 'TENTH',
        11, 'INTERMEDIATE 1',
        12, 'INTERMEDIATE 2'
    )
]

GRADE_SUBJECTS = [
    ('math', 'Mathematics'),
    ('english', 'English'),
    ('science', 'Science'),
    ('social_studies', 'Social Studies'),
    ('language', 'Language'),
    ('physical_education', 'Physical Education'),

]

INTERMEDIATE_SUBJECTS = [
    ('math', 'Mathematics'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('biology', 'Biology'),
    ('computer_science', 'Computer Science'),
    ('english', 'English'),
    ('physical_education', 'Physical Education'),
]


COMPUTER_SCIENCE_TOPICS = [
    ('programming', 'Programming'),
    ('algorithms', 'Algorithms'),
    ('data_structures', 'Data Structures'),
    ('networking', 'Networking'),
    ('database', 'Database Systems'),
    ('web_development', 'Web Development'),
    ('artificial_intelligence', 'Artificial Intelligence'),
]

INTRESTS_CHOICES = GRADE_SUBJECTS + INTERMEDIATE_SUBJECTS+ COMPUTER_SCIENCE_TOPICS


APTITUDE_CHOICES = [
    ('mathematical', 'Mathematical Aptitude'),
    ('logical', 'Logical Reasoning'),
    ('verbal', 'Verbal Aptitude'),
    ('artistic', 'Artistic Aptitude'),
    ('creative', 'Creative Thinking'),
    ('technical', 'Technical Skills'),
    ('analytical', 'Analytical Skills'),
    ('problem_solving', 'Problem Solving'),
]


# Update the Student model to include the aptitudes field
class Student(models.Model):
    name           = models.CharField(max_length=30)
    uid            = models.CharField(max_length=10, default=str(uuid.uuid4())[:8])
    studentID      = models.CharField(max_length=10, unique=True, error_messages={'unique': "A user with that ID already exists."})
    password       = models.CharField(max_length=128)
    phoneNumber    = models.CharField(max_length=10, unique=True)
    parentNumber   = models.CharField(max_length=10)
    profilePic     = models.ImageField(upload_to="users/assets/images")
    grade          = models.IntegerField(default=8)

    # Add multiple aptitudes (similar to interests)
    aptitudes      = models.CharField(
                        max_length=500,  # You can adjust the length as necessary
                        choices=APTITUDE_CHOICES,
                        blank=True,
                        null=True
                    )

    interests      = models.CharField(
                        max_length=500,  # You can adjust the length as necessary
                        choices=INTRESTS_CHOICES,
                        blank=True,
                        null=True
                    )

    def __str__(self):
        return self.name

    assignments_completed = models.ManyToManyField(
        Assignment,
        through='assignments.CompletedAssignment',
        related_name='students'
    )


    def save(self, *args, **kwargs):
            # Hash the password before saving
            if not str(self.password).startswith('pbkdf2_'):  # Prevent re-hashing if already hashed
                self.password = make_password(self.password)
            super(Student, self).save(*args, **kwargs)


DEPT_CHOICES = (
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electrical and Computer Engineering"),
    ("EEE", "Electrical and Electronic Engineering"),
    ("MECH", "Mechanical Engineering"),
)

class Lecturer(models.Model):
    uid            = models.CharField(max_length=30,default=str(uuid.uuid4())[:8])
    name            =  models.CharField(max_length=30, name="Name",default="")
    id              =  models.CharField(max_length=10, name="mID",default="")
    phoneNumber     =  models.CharField(max_length=10, name="Phone number",default="")
    profilePic      =  models.ImageField(name="Photo",default="")
    Department      =  models.CharField(max_length=41,choices=DEPT_CHOICES,default="CSE")

    def __str__(self):
        return self.name


class Parent(models.Model):
    name           = models.CharField(max_length=30)
    studentID      = models.CharField(max_length=10, unique=True, error_messages={'unique': "A user with that ID already exists."})
    phoneNumber    = models.CharField(max_length=10, unique=True)
