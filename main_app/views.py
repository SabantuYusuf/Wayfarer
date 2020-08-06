from django.shortcuts import render, redirect
from .models import Profile, Post
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login
from .forms import UserRegisterForm, ProfileRegisterForm, PostForm


# Create your views here.

# Temp data
# class Post:
#   def __init__(self, title, author, content, city):
#     self.title = title
#     self.author = author
#     self.content = content
#     self.city = city

# posts = [
#   Post('Big Ben got Booty', 'Some Guy', 'Dang BB is huge and keeps correct time? You go, Ben Coco!', 'London'),
#   Post('Tour Busses - Watch Your Head!', 'Guy #2', 'Hit my head going under a tree. 2/10', 'London'),
#   Post('Phone Booths Still Exist?', 'Some Girl!', 'Did not know these still existed. Went in one to make a call and realized it was disconnected', 'London'),
# ]

# Home
def home(request):
	return render(request, 'home.html')

# User Routes
def signup(request):
  error_message = ''
  form = UserRegisterForm(request.POST)
  p_reg_form = ProfileRegisterForm(request.POST)
  if request.method == 'POST':
    if form.is_valid() and p_reg_form.is_valid():
      user = form.save()
      profile = p_reg_form.save(commit=False)
      profile.user = user
      profile.save()
      login(request, user)
      return redirect('profile', user.id)
    else:
      error_message = 'Invalid sign up - try again'
      form = UserRegisterForm()
      p_reg_form = ProfileRegisterForm()
  context = {
    'form': form, 
    'p_reg_form': p_reg_form,
    'error_message': error_message,
  }
  return render(request, 'registration/signup.html', context)

# Profile
# def profile(request, user_id, #post_id):
def profile(request, user_id):
  current_user = Profile.objects.get(user=user_id)
  # post = Post.objects.get(post_id=post_id)
  context = {
    'profile': current_user
    # 'post': post
  }
  return render(request, 'users/profile.html', context)


# Create (New) Post Route
def new_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
    # image = request.POST['image']
      new_post = post_form.save(commit=False)
      # user = Profile.ojects.get(user_id=user_id)
      new_post.user = request.user
      new_post.save()

      # return redirect('profile', new_post.id)
      return redirect('post_show', new_post.id)
  else:
    post_form = PostForm()
    return render(request, 'posts/new.html', {'post_form': post_form})

# Post Show Page
def post(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {
    'post': post
    }
  return render(request, 'posts/postsshow.html', context)


# City Route
def cities(request):
	return render(request, 'cities.html')
