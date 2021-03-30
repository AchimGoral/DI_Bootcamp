from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from . import urls
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def blog_view(request):
    return render(request, 'blog.html', {'posts': Post.objects.published()})

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
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)

        # Check if user has already liked the post
        if post.likes.filter(id=request.user.profile.id).exists():
            post.likes.remove(request.user.profile)
            flag = False
        else:
            post.likes.add(request.user.profile)
            flag = True
        result = post.sum_likes()
        post.save()

        return JsonResponse({'result': result, 'id':id, 'flag': flag})

# @login_required
# def blog_likes_view(request):
#     liked = User.profile.prefetch_related('blog_like').get(pk=1).blog_like.all()
#     return render(request, 'blog_likes.html', {'liked': liked})