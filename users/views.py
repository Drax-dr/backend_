from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Student, Lecturer
from.forms import LoginForm, StudentRegistrationForm


class HomeView(TemplateView):
    template_name = "home.html"

class RegisterView(TemplateView):
    template_name = 'register.html'

class StudentRegisterView(TemplateView):
    template_name = 'student/register.html'

class LecturerRegisterView(TemplateView):
    template_name = 'register.html'

class UserDasboardView(TemplateView):
    model = Student
    template_name = "student/student-dashboard.html"

class LecturerDashboardView(TemplateView):
    model = Lecturer
    template_name = "lecturer/educator-dashboard.html"

class AdminProfileView:
    pass

def login_student(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            studentID = form.cleaned_data['studentID']
            password = form.cleaned_data['password']

            try:
                student = Student.objects.get(studentID=studentID)
                if check_password(password, student.password):
                    request.session['student_id'] = student.id  # Save student ID in session
                    messages.success(request, 'Login successful.')
                    return redirect('dashboard')  # Redirect to a student dashboard or home page
                else:
                    messages.error(request, 'Invalid password.')
            except Student.DoesNotExist:
                messages.error(request, 'Student ID not found.')
    else:
        form = LoginForm()

    return render(request, 'register.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Student instance without saving to hash the password first
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()  # Save the hashed password instance to the database
            messages.success(request, 'Registration successful.')
            return redirect('login')  # Redirect to a login page or another page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'studentID', 'phoneNumber', 'ParentNumber', 'profilePic', 'grade', 'assignments_completed']
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'studentID', 'phoneNumber', 'ParentNumber', 'profilePic', 'grade', 'assignments_completed']
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


# Views for Lecturer
class LecturerListView(ListView):
    model = Lecturer
    template_name = 'lecturer_list.html'
    context_object_name = 'lecturers'


class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = 'lecturer_detail.html'
    context_object_name = 'lecturer'


class LecturerCreateView(CreateView):
    model = Lecturer
    template_name = 'lecturer_form.html'
    fields = ['Name', 'mID', 'Phone number', 'Photo']
    success_url = reverse_lazy('lecturer_list')


class LecturerUpdateView(UpdateView):
    model = Lecturer
    template_name = 'lecturer_form.html'
    fields = ['Name', 'mID', 'Phone number', 'Photo']
    success_url = reverse_lazy('lecturer_list')


class LecturerDeleteView(DeleteView):
    model = Lecturer
    template_name = 'lecturer_confirm_delete.html'
    success_url = reverse_lazy('lecturer_list')
