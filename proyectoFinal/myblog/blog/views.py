from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Article
from .forms import CommentForm

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()  # Obtiene todos los comentarios asociados a este artículo
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()
    return render(request, 'article_detail.html', {'article': article, 'comments': comments, 'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
