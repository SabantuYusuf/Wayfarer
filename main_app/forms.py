from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['city', 'prof_img']

# Edit Profile
class EditProfile(forms.ModelForm):

    class Meta:
 	    model = User
 	    fields = ['first_name', 'last_name']

class EditProfileCity(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['city', 'prof_img']
        
# Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'city_options', 'post_img']


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_img']



