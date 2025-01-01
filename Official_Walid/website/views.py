from django.shortcuts import render, redirect
from .models import Article, YoutubeVideos
import markdown2
from .forms import ArticleForm, YtbVids
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(requst):
    articles = Article.objects.all().order_by('-created_at')
    artiles1 = articles[:3]
    artiles2 = articles[3:6]
    articles6 = articles[:6]

    videos = YoutubeVideos.objects.all().order_by('-created_at')
    videos1 = videos[:3]
    videos2 = videos[3:6]
    videos6 = videos[:6]
    return render(requst, 'website/index.html', {
        'articles1':artiles1,
        'articles2':artiles2,
        'articles6': articles6,
        'videos1': videos1,
        'videos2': videos2,
        'videos6':videos6

    })

def articles_view(requst, id):
    article = Article.objects.get(pk=id)
    pdfID = article.pdfID
    pdfID = pdfID.split('/')[5]
    article.readCount += 1
    article.save()
    html_content = markdown2.markdown(article.content)
    return render(requst, 'website/articles.html', {
        'article' : article,
        'content' : html_content,
        'pdfid' : pdfID,
    })


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Set the logged-in user as the author
            article.save()
            messages.success(request, 'Article created successfully!')
            return redirect('index')  # Replace 'articles' with your desired URL name
    else:
        form = ArticleForm()

    return render(request, 'website/create_article.html', {'form': form})


@login_required
def create_video(request):
    if request.method == 'POST':
        form = YtbVids(request.POST)
        if form.is_valid():
            youtubeVideo = form.save(commit=False)
            youtubeVideo.save()
            messages.success(request, 'Article created successfully!')
            return redirect('index')  # Replace 'articles' with your desired URL name
    else:
        form = YtbVids()

    return render(request, 'website/create_video.html', {'form': form})


def allArticles(request):
    if request.method == 'POST':
        searchFor = request.POST.get('search-For', '')
        allArticles = Article.objects.all()
        articles = []
        for article in allArticles :
            if searchFor in article.title:
                articles.append(article)
        
        return render(request, 'website/allArticles.html', {
        'articles':articles,
        })

    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'website/allArticles.html', {
        'articles':articles,
    })