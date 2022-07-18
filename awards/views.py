from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile,Project,Comment,Ratings
from .serializer import ProfileSerializer, ProjectSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


def index(request):
    projects = Project.objects.all()
    context={
        'projects' : projects,
    }
    return render(request,"index.html", context)
    

def register(request):
    form=RegisterUserForm

    if request.method =='POST':
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("registration successful"))
        
            return redirect('login')
    context={'form':form}

    return render(request,'registration/register.html',context)

def login_in(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("login successful"))
            return redirect('profile')
        
    context={}
    return render(request,'registration/login.html')

def log_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    profiles=Profile.objects.get(user=request.user)
    projects=Project.objects.filter(user=request.user)
       
    context={
        'projects':projects,
        'profiles':profiles, 
        }
    
    return render(request,'profile.html',context )

@login_required(login_url='login')
def update_profile(request):
    profiles = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return redirect('profile')
       
    else:
        
        prof_form = UpdateProfileForm(instance=request.user.profile)
             
    context={
      
        'prof_form': prof_form,
        'profiles':profiles,
        
        }
    
    return render(request, 'update_profile.html',context)

@login_required(login_url='login')
def upload_project(request):
    current_user = request.user
    projects = Project.objects.all()
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadProjectForm(request.POST,request.FILES)
                if form.is_valid():
                    new_project = form.save(commit=False)
                    new_project.user = current_user
                    new_project.profile = profile
                    new_project.save()
                    print(new_project)
                    return redirect('home')
            else:
                form = UploadProjectForm()
                
            context = {
                'user':current_user,
                'form':form,
                'projects':projects,
                
            }
            return render(request,'upload_project.html', context)










    # projects = Project.objects.all()
    # users = User.objects.exclude(id=request.user.id)
    # if request.method == 'POST':
    #     form = UploadProjectForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user.profile
    #         post.save()
    #         return redirect('index')
    # else:
    #     form = UploadProjectForm()
    # context = {
    #     'projects': projects,
    #     'form': form,
    #     'users': users,
    # }
    # return render(request, 'upload_project.html',context)

@login_required(login_url='login')
def rating(request,id):
    project=Project.objects.get(id=id)
    rating=Ratings.objects.filter(project=project)
    print(rating)
    # project = get_object_or_404(Project,pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data["design_rating"]
            usability_rating = form.cleaned_data["usability_rating"]
            content_rating = form.cleaned_data["content_rating"]
            comment = form.cleaned_data["comment"]
            rating = form.save(commit=False)
            rating.project = project
            rating.author = current_user
            rating.design_rating = design_rating
            rating.usability_rating = usability_rating
            rating.content_rating = content_rating
            rating.comment = comment
            rating.save()
            return redirect ('home')
        
    else:
        form = RatingForm()

        context={
            'project' : project,
            'form' : form,
            'ratings':rating}
    return render(request,'rating.html',context ) 

def project_search(request):
    if 'project' in request.GET and request.GET["project"]:
    # if request.method == 'GET':
        search_term= request.GET.get("project")
        results = Project.search_project(search_term)
        print(results)
        message = f'search_term'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})

class ProfileViewSet(APIView):
    def get(self, request, format=None):
        queryset = Profile.objects.all()
        # serializer_class = ProfileSerializer(all_profile, many=True)
        # return Response(serializers.data)



class ProjectViewSet(APIView):
    def get(self, request, format=None):
        queryset = Project.objects.all()
        serializer_class = ProjectSerializer
        # return Response(serializers.data)


