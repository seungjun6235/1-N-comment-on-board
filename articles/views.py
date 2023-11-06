from django.shortcuts import render, redirect
from .models import Article,Comment 
from .forms import ArticleForm,CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context={
        'articles': articles,
    }

    return render(request,'index.html',context)

def detail(request,id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    #Comment 목록 조회

    #첫번째 방법
    # comments = Comment.objects.filter(article=article)

    #두번째 방법
    # comments = article.comment_set.all()

    #세번째 방법
    #HTML코드에서 article.comment_set.all()사용

    context={
        'article' : article,
        'form' : form,
        # 'comments': comments,
    }

    return render(request,'detail.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id= article.id)
    else:
        form = ArticleForm()

    context ={
        'form': form
    }

    return render(request, 'form.html', context)


def comment_create(request, article_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        #form을 저장 => 추가로 넣어야하는 데이터를 넣기 위해 저장 멈추기
        comment = form.save(commit=False)

        #첫번째 방법
        #article_id를 기준으로 article obj 가져오기
        # article = Article.objects.get(id=article_id)
        # #article 컬럼에 추가
        # comment.article = article
        # comment.save()

        #두번째 방법(integer를 저장하는 방법)
        comment.article_id= article_id
        comment.save()

        return redirect('articles:detail',id=article_id)