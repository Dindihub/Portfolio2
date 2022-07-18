from unittest import TestResult
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',default='default.png')
    bio = models.TextField(max_length=100)
    contact=models.IntegerField(default=0)
    email=models.EmailField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        db_table = 'profiles'
        ordering = ['-id']


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    project_image = CloudinaryField('project_image',null=True)
    project_title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000,  null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    date_posted = models.DateTimeField(auto_now_add=True)
    project_url=models.CharField(max_length=200,null=True)
    like = models.PositiveIntegerField(default=0)
    
    def __str__(self):
            return self.project_title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects
    
    @classmethod
    def search_project(cls,search_term):
        return cls.objects.filter(project_title__icontains=search_term).all()

    class Meta:
        db_table = 'projects'
        ordering = ['-id'] 

class Comment(models.Model):
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    date_posted = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_comment')        
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()

    class Meta:
        db_table = 'comments'
        ordering = ['-id']    
        
class Ratings(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings',null=True)
    design_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    # def __str__(self):
    #     return self.author        
    
    def save_rating(self):
            self.save()

    def get_rating(self, id):
        comments = Ratings.objects.filter(project_id =id)
        return comments
    
    @classmethod
    def get_ratings(cls):
        ratings = Ratings.objects.all()
        return ratings

