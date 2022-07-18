from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Comment,Ratings
from django.forms import ModelForm, TextInput, EmailInput,ImageField, Textarea



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image','bio','contact','email')
        # widgets = {
        #     'image':forms.ImageField(attrs={
        #         'class': "form-control",
        #         }),
        #     'bio':forms.Textarea(attrs={
        #         'class': "form-control", 
        #         'placeholder': 'bio',
        #         }),
        #     'email':forms.EmailInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email',
        #         })
        # }



class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_image','project_title','description','like','project_url')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        design_rating = forms.IntegerField()
        usability_rating = forms.IntegerField()
        content_rating = forms.IntegerField()
        comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Leave a comment"}))    
        exclude =['project','author']    
