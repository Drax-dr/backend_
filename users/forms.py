from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'studentID', 'password', 'phoneNumber', 'parentNumber', 'profilePic', 'grade']

    def clean_studentID(self):
        studentID = self.cleaned_data.get('studentID')
        if Student.objects.filter(studentID=studentID).exists():
            raise forms.ValidationError("A student with that ID already exists.")
        return studentID

    def clean_phoneNumber(self):
        phoneNumber = self.cleaned_data.get('phoneNumber')
        if Student.objects.filter(phoneNumber=phoneNumber).exists():
            raise forms.ValidationError("A student with that phone number already exists.")
        return phoneNumber

class LoginForm(forms.Form):
    studentID = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
