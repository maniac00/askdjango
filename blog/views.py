from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from .forms import PostForm, PostForm2, CommentForm
from .models import Post, Comment

index = ListView.as_view(model=Post, paginate_by=5)

def post_new(request):
    if request.method == 'POST':
        form = PostForm2(request.POST)
        if form.is_valid():

            #name = form.cleaned_data['name']
            #desc = form.cleaned_data['desc']
            #post = Post(name=name, desc=desc)
            post = form.save()
            messages.info(request, "새 포스팅이 등록되었습니다.")
            return redirect(post)
    else:
        form = PostForm2()

    print(request.GET)
    print(request.POST)
    print(request.FILES)
    return render(request, 'blog/form.html', {'form':form})

# def index(request):
#    response = render(request, 'blog/index.xml', content_type = 'text/xml')
#    return response

 #  return render(request, 'blog/index.html')
# Create your views here.
def post_detail(request, pk=None, name=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
    elif name:
        post = get_object_or_404(Post, pk=name)
    else:
        raise Http404

    return render(request, 'blog/post_detail.html', {'post': post})



def list_by_day(request, year, month=None, day=None):
    pass

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.info(request, "새 댓글이 등록되었습니다.")
            return redirect(comment.post)
    else:
        form = CommentForm()

    return render(request, 'blog/form.html', {'form':form})

@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk, post__id=post_pk)
    if comment.author != request.user:
        redirect_url = request.META.get('HTTP_REFERER', settings.LOGIN_URL)
        messages.warning(request, '작성자만 댓글을 수정할 수 있습니다.')
        return redirect(redirect_url)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.info(request, "댓글이 수정되었습니다.")
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/form.html', {'form':form})