from rest_framework import serializers
from .models import Profile, Project
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio', 'bio', 'contact','email']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title','project_image','user', 'description', 'project_url', 'date_posted']