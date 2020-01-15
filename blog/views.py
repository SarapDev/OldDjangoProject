from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.

def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post. objects.all()

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context={
        'page_object': page,
        'is_paginated': is_paginated,
        'next_page': next_url,
        'prev_page': previous_url
    }

    return render(request, 'blog/index.html', context=context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

    def comment_lis(self, request, template):
        comment = Comment.objects.all()
        return render(request, template, contex={'comment': comment})

class CommentCreate(LoginRequiredMixin, ObjectCreateMixin, PostDetail,View):
    model = CommentForm
    template = PostDetail.template

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class PostChange(LoginRequiredMixin, ObjectChangeMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_change_form.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class TagChange(LoginRequiredMixin, ObjectChangeMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_change_form.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True

class CommentCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = CommentForm
    template = 'blog/post_detail.html'
    redirect_url = 'post_list_url'
