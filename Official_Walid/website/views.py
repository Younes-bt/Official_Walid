from django.shortcuts import render, redirect
from .models import Article
import markdown2
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(requst):
    return render(requst, 'website/index.html')

def articles_view(requst, id):
    article = Article.objects.get(pk=id)
    html_content = markdown2.markdown(article.content)
    return render(requst, 'website/articles.html', {
        'article' : article,
        'content' : html_content,
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