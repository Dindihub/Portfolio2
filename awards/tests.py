from django.test import TestCase
from.models import *

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(username='sandra')
        self.user.save()

        self.profile_test = Profile(id=1, user=self.user , image='default.jpg', bio='this is a test profile',
                                    contact='image',email='email')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.project = Project.objects.create(id=1, project_title='test project', project_image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, project_url='http://ur.coml')
    
    
        self.project_test = Project(id=1, user=self.user , project_image='default.jpg', description='this is a test profile',
                                    project_title='image',project_url='url')
                                    
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    
    def test_save_project(self):
        self.project_test.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.project_test.delete_image()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

    def test_search_project(self):
        self.project_test.save()
        project = Project.search_project('test')
        self.assertTrue(len(project) > 0)

class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.comment = Comment.objects.create(id=1, content='comment',
                                        user=self.user)
    
    
        self.comment_test = Comment(id=1, user=self.user , content='comment')
    def test_save_comment(self):
        self.comment_test.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0) 

class RatingsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.project = Project.objects.create(id=1, project_title='test post', project_image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, project_url='http://ur.coml')
        self.rating_test = Ratings.objects.create(id=1,comment='comment', design_rating=6, usability_rating=7, content_rating=9, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Ratings))

    def test_save_rating(self):
        self.rating_test.save_rating()
        ratings = Ratings.objects.all()
        self.assertTrue(len(ratings) > 0)

    def test_get_rating(self, id):
        self.rating_test.save()
        rating = Ratings.get_ratings(project_id=id)
        self.assertTrue(len(rating) == 1)                              



