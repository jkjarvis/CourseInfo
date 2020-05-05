from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course


class CourseInfo(forms.ModelForm):

    class Meta:
        model = Course
        fields = {'title', 'link', 'teacher', 'SubjectField', 'rating'}
    field_order = ['title', 'teacher', 'SubjectField', 'link', 'rating']

