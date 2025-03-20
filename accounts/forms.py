from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError
from .models import Profile
from news.models import Category, Tag, Article


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if len(password) > 20:
            raise ValidationError("Password must be no more than 20 characters long.")
        return password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("The username or password is incorrect.", code='invalid_info')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'image')


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'image', 'publish']


class CreateTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'category', 'title', 'slug', 'description', 'tags', 'image', 'publish']


