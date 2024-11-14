from django.contrib import admin

from users.models import Student, Lecturer, Parent

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Parent)
