from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm, ProfileEditForm, CreateCategory, CreateTag, CreateArticle
from .models import Profile
from news.models import Article, Category, Tag
from django.core.paginator import Paginator


def user_register(request):
    if request.user.is_authenticated:
        return redirect('news:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # تنظیم پسورد
            user.save()  # ذخیره کاربر
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('news:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('news:home')


# dashboard view

@login_required
def dashboard(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    return render(request, 'dashboard/dashboard.html', {'profiles': profiles})


def get_pages_to_show(current_page, total_pages):
    """Utility function to determine which pagination pages to show."""
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def profile_list(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    profiles_list = Profile.objects.all().order_by('-created_at')
    page_number = request.GET.get('page')
    paginator = Paginator(profiles_list, 5)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/profile_list.html', {'profiles_list': object_list, 'profiles': profiles,
                                                           'pages_to_show': pages_to_show})


def edit_user_profile(request, username):
    user = request.user
    profiles = Profile.objects.get(user=user)
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_list')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'dashboard/edit_profile.html', {'profiles': profiles, 'form': form})


def edit_profile(request, username):
    user = request.user
    profiles = Profile.objects.get(user=user)
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'dashboard/edit_profile.html', {'profiles': profiles, 'form': form})


def delete_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    profile.delete()
    user.delete()
    return redirect('accounts:profile_list')


def category_list(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    categories = Category.objects.all().order_by('-created_at')
    page_number = request.GET.get('page')
    paginator = Paginator(categories, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/category_list.html', {'profiles': profiles, 'categories': object_list,
                                                            'pages_to_show': pages_to_show})


def category_create(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    if request.method == 'POST':
        forms = CreateCategory(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('accounts:category_list')
    else:
        forms = CreateCategory()
    return render(request, 'dashboard/category_create.html', {'profiles': profiles, 'forms': forms})


def category_edit(request, slug):
    user = request.user
    profiles = Profile.objects.get(user=user)
    categories = get_object_or_404(Category, slug=slug)
    forms = CreateCategory(request.POST or None, request.FILES or None, instance=categories)
    if forms.is_valid():
        forms.save()
        return redirect('accounts:category_list')
    return render(request, 'dashboard/category_edit.html', {'profiles': profiles, 'categories': categories, 'forms': forms})


def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.delete()
    return redirect('accounts:category_list')


def category_search(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    categories_search = request.GET.get('search')
    categories = Category.objects.filter(title__icontains=categories_search)
    page_number = request.GET.get('page')
    paginator = Paginator(categories, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/category_list.html', {'profiles': profiles, 'categories': object_list,
                                                            'pages_to_show': pages_to_show})


def tag_list(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    tags = Tag.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(tags, 10)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/tag_list.html', {'profiles': profiles, 'tags': object_list,
                                                       'pages_to_show': pages_to_show})


def tag_create(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    if request.method == 'POST':
        forms = CreateTag(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('accounts:tag_list')
    else:
        forms = CreateTag()
    return render(request, 'dashboard/tag_create.html', {'profiles': profiles, 'forms': forms})


def tag_edit(request, title):
    user = request.user
    profiles = Profile.objects.get(user=user)
    tags = get_object_or_404(Tag, title=title)
    forms = CreateTag(request.POST or None, instance=tags)
    if forms.is_valid():
        forms.save()
        return redirect('accounts:tag_list')
    return render(request, 'dashboard/tag_edit.html', {'profiles': profiles, 'tags': tags, 'forms': forms})


def tag_delete(request, title):
    tag = get_object_or_404(Tag, title=title)
    tag.delete()
    return redirect('accounts:tag_list')


def tag_search(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    tags_search = request.GET.get('search')
    tags = Tag.objects.filter(title__icontains=tags_search)
    page_number = request.GET.get('page')
    paginator = Paginator(tags, 10)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/tag_list.html', {'profiles': profiles, 'tags': object_list,
                                                       'pages_to_show': pages_to_show})


def article_list(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    articles = Article.objects.all().order_by('-created_at')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/article_list.html', {'profiles': profiles, 'articles': object_list,
                                                           'pages_to_show': pages_to_show})


def article_create(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    if request.method == 'POST':
        forms = CreateArticle(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('accounts:article_list')
    else:
        forms = CreateArticle()
    return render(request, 'dashboard/article_create.html', {'profiles': profiles, 'forms': forms})


def article_edit(request, slug):
    user = request.user
    profiles = Profile.objects.get(user=user)
    articles = get_object_or_404(Article, slug=slug)
    forms = CreateArticle(request.POST or None, request.FILES or None, instance=articles)
    if forms.is_valid():
        forms.save()
        return redirect('accounts:article_list')
    return render(request, 'dashboard/article_edit.html', {'profiles': profiles, 'articles': articles, 'forms': forms})


def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('accounts:article_list')


def article_search(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    articles_search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=articles_search)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'dashboard/article_list.html', {'profiles': profiles, 'articles': object_list,
                                                           'pages_to_show': pages_to_show})
