from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Categori
from .forms import Postform, CommentForm, CategoriForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def  sign_up(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect(post_list)
    else:
        userform = UserCreationForm()

    return render(request, 'blog/sign_up.html', {'userform':userform,})

@login_required
def post_list(request):
    posts = Post.objects.all()
    categoris = Categori.objects.all()
    if request.method == "GET":
        try:
            categori = request.GET['categori']
        except:
            categori = "all"
    return render(request, 'blog\post_list.html', {'post': posts, 'categoris': categoris})

def post_delete(request):
    pk = request.GET['pk']
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect(post_list)
    #else:
     #   return redirect(post_detail, pk=pk)

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.author = request.user
            comment.post = posts
            comment.created_date = timezone.now()
            comment.save()
            return redirect(post_detail, pk=pk)
    commentForm = CommentForm()
    comments = Comment.objects.filter(post=pk)
    return render(request, 'blog/post_detail.html',{'post':posts, 'comments':comments, 'commentForm': commentForm})

def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        categoriForm = CategoriForm(request.POST)
        if form.is_valid():
            categori = categoriForm.save(commit=False)
            try:
                categori = Categori.objects.get(categori_name=categori.categori_name)
            except Categori.DoesNotExist:
                categori.save()
            post = form.save(commit=False)
            post.categori = categori
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = Postform()
        categoriForm = CategoriForm()
    return render(request, 'blog/post_edit.html', {'form':form, 'categoriForm': categoriForm})

# Create your views here.
