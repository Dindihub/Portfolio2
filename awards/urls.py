from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',views.index,name = 'home'),
    path('register',views.register,name='register'),
    path('login',views.login_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('upload_project', views.upload_project, name='upload_project'),
    path('search', views.project_search, name='search'),
    path ('rating/<str:id>/',views.rating,name='rating'),
    

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
# (\d+)/