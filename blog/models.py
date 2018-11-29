from django.db import models
from django.utils import timezone

#post라는 모델을 만드는것
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categori = models.ForeignKey('blog.Categori', null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)#날짜를 지정하는
    published_date = models.DateTimeField(
        blank=True, null=True)#blank=True는 빈칸으로 나눠도 상관 없다는
    #글쓴이, 제목, 내용, 만든날짜, 출판날짜를 무조건 써주도록 하는

    #발행하는 함수를 더 만듦
    def publish(self):
        self.published_date = timezone.now()#발행한 날짜를 따로 선언
        self.save()#저장을 해주는

    #class의 형식이 아니라 아래의 형식대로 출력되도록 하는 것
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200, null = True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Categori(models.Model):
    categori_name = models.CharField(max_length=200)

    def __str__(self):
        return self.categori_name
