from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 자동생성 해줌 컬럼 여러개의 데이터 comment_set =

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    # 컬럼 한개의 데이터 article_id를 자동으로 생성하줌 장고가

