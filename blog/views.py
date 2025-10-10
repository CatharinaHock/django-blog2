from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Tag, Comic
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, 'blog/post_list.html', {"posts":posts}) # referenz zu blog/templates/blog/post_list.html

def post_list_filtered(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts=Post.objects.filter(tags__pk=pk)
    return render(request, 'blog/post_list_filtered.html', {"posts":posts, "tag":tag})

@login_required
def post_draft_list(request):
    posts=Post.objects.filter(published_date__isnull=True).order_by("created_date")
    return render(request, 'blog/post_draft_list.html', {"posts":posts}) # referenz zu blog/templates/blog/post_list.html


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk = post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/post_detail.html", {"post":post, "form":form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk = post.pk)
    else: 
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
    return render(request, "blog/about.html", {})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')

"""
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk = post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment_to_post.html", {"form":form})
"""

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def comic_detail(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    """
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk = post.pk)
    else:
        form = CommentForm()
     """
    
    previous_pk = max(pk-1,1) 
    next_exists = Comic.objects.filter(pk=pk + 1).exists()
    next_pk = pk + 1 if next_exists else pk

    return render(request, "blog/comic_detail.html", {"comic":comic,"next_pk":next_pk, "previous_pk": previous_pk})# "form":form})

def comic_list(request):
    comics=Comic.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, 'blog/comic_list.html', {"comics":comics})