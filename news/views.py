from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag
from .forms import MessageForm, SubscriberForm
from django.http import JsonResponse
from django.template.defaultfilters import truncatewords


def home(request):
    latest_articles = Article.objects.filter(publish=True).order_by('-created_at')[:5]
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    political_articles = Article.objects.filter(publish=True, category__title='Political').order_by('-created_at')[:3]
    older_political_articles = Article.objects.filter(publish=True, category__title='Political').order_by('-created_at')[:4]
    categories = Category.objects.filter(publish=True)
    return render(request, 'news/home.html',
                  {'latest_articles': latest_articles, 'popular_articles': popular_articles, 'new_article': new_article,
                   'categories': categories, 'political_articles': political_articles,
                   'older_political_articles': older_political_articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    tags = Tag.objects.all()
    article.views += 1
    article.save()
    return render(request, 'news/article_detail.html', {'article': article, 'popular_articles': popular_articles,
                                                        'new_article': new_article, 'tags': tags})


def article_list(request):
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    page = int(request.GET.get('page', 1))
    per_page = 5
    start = (page - 1) * per_page
    end = start + per_page

    articles = Article.objects.filter(publish=True).order_by('-created_at')
    total_count = articles.count()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        articles_page = articles[start:end]
        data = []
        for article in articles_page:
            truncated_description = truncatewords(article.description, 20)
            data.append({
                'title': article.title,
                'description': truncated_description,
                'image_url': article.image.url,
                'url': article.get_absolute_url(),
                'created_at': article.created_at.strftime('%Y-%m-%d')
            })
        return JsonResponse({
            'articles': data,
            'has_more': total_count > end
        })

    articles_page = articles[start:end]
    return render(request, 'news/article_list.html', {'popular_articles': popular_articles, 'new_article': new_article,
                                                      'articles': articles_page,
                                                      'has_more': total_count > end})


def article_search(request):
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    articles_search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=articles_search)
    return render(request, 'news/article_list.html', {'popular_articles': popular_articles, 'new_article': new_article,
                                                      'articles': articles})


def category_list(request):
    categories = Category.objects.filter(publish=True)
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    return render(request, 'news/category_list.html', {'categories': categories, 'popular_articles': popular_articles,
                                                       'new_article': new_article})


def category_article(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(publish=True, category=categories)
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    return render(request, 'news/category_article.html', {'categories': categories, 'articles': articles,
                                                          'popular_articles': popular_articles,
                                                          'new_article': new_article})


def article_tag(request, title):
    tags = Tag.objects.all()
    active_tag = get_object_or_404(Tag, title=title)
    articles = active_tag.articles.all()
    popular_articles = Article.objects.filter(publish=True).order_by('-views')[:4]
    new_article = Article.objects.filter(publish=True).order_by('-created_at')[0]
    return render(request, 'news/article_tag.html', {'tags': tags, 'active_tag': active_tag, 'articles': articles,
                                                     'popular_articles': popular_articles, 'new_article': new_article})


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:home')
    else:
        form = MessageForm()
    return render(request, 'news/contact.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:home')
