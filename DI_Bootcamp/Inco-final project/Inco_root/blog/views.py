from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from . import urls
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

def home_view(request):
    return render(request, 'home.html')

def blog_view(request):
    categories = Category.objects.all()
    posts = Post.objects.published()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'blog.html', context)

def category_view(request, pk):
    categories = Category.objects.all()
    posts = Post.objects.category(pk=pk)
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'blog.html', context)

def blog_draft_view(request):
    return render(request, 'blog_drafts.html', {})

def blog_entry_view(request, pk):

    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        comment_form = CommentForm()
        context = {
            'post':post,
            'comment_form':comment_form
        }
        return render(request,'blog_entry.html',context)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.profile = request.user.profile
            comment.post = Post.objects.get(id=pk)
            comment.save()
            return redirect('blog-entry', pk)

@login_required
def new_entry_view(request):

    if request.method == 'GET':
        return render(request,'new_entry.html',{'my_form':PostForm()})

    if request.method == 'POST':
        my_form = PostForm(request.POST)

        if my_form.is_valid():
            post = my_form.save(commit=False)
            post.profile = request.user.profile
            post.save()
            return redirect('blog')
        else:
            return render(request,'new_entry.html',{'my_form':PostForm()})

@login_required
def blog_edit_view(request, pk):

    if request.method == 'GET':
        edit_post = Post.objects.get(id=pk)
        return render(request,'new_entry.html',{'my_form':PostForm(instance=edit_post)})

    if request.method == 'POST':
        edit_post = Post.objects.get(id=pk)
        my_form = PostForm(request.POST, instance=edit_post)

        if my_form.is_valid():
            post = my_form.save(commit=False)
            post.profile = request.user.profile
            post.save()
            return redirect('blog-drafts')
        else:
            return render(request,'new_entry.html',{'my_form': my_form})

@login_required
def blog_delete_view(request, pk):

    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('blog')

@login_required
def blog_like_view(request):
    
    if request.POST.get('action') == 'post':
        result = 0
        id = int(request.POST.get('post_id'))
        post = get_object_or_404(Post, id=id)

        if post.likes.filter(id=request.user.profile.id).exists():
            post.likes.remove(request.user.profile)
            text = 'far fa-heart'
        else:
            post.likes.add(request.user.profile)
            text = 'fas fa-heart'
        result = post.sum_likes()
        post.save()

        return JsonResponse({'result': result, 'id': id, 'text': text})