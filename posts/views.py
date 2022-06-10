
from taggit.models import Tag
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import ShareForm, CommentForm
from posts.models import *


def index (request , tag_slug=None):


# ─── FUANCTONS ──────────────────────────────────────────────────────────────────

    query = None
    page = None
    posts = card.objects.all()
# ─── TAG ────────────────────────────────────────────────────────────────────────


    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__name__in=[tag])

# ─── SEARCH ─────────────────────────────────────────────────────────────────────

    if "q" in request.GET:
        query = request.GET['q']
        posts = posts.filter(body__contains=query)
# ─── PAGINATION ─────────────────────────────────────────────────────────────────

    paginator = Paginator(posts, 16)
    if "page" in request.GET:
        page = request.GET['page']
    try:
        paginator_posts = paginator.page(page)
    except EmptyPage :
        paginator_posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger: 
        paginator_posts = paginator.page(1)
# ─── END PAGINATION ──────────────────────────────────────────────

    context = {'posts' : paginator_posts }
    return render(request, 'posts/Pages/index.html' , context)
# ─── POST VIEW DETAILS ──────────────────────────────────────────────────────────

def post_view_details(request , year,month,day,slug):
    post = get_object_or_404(
        card,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
        slug=slug
         )
    comments = post.comments.all().filter(active=True)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Comment shared to post')
            comment_form = CommentForm()
    context = {'post' : post,  'comments' : comments , "comment_form" : comment_form}
    return render(request, 'posts/Pages/post_view_details.html' , context)

# ─── TAG VIEW ───────────────────────────────────────────────────────────────────

def category_view(request):
    tags = Tag.objects.all()
    context = {'tags' : tags}
    return render(request, 'posts/Pages/category_view.html' , context)

def share(request, year,month,day,slug):
    post = get_object_or_404(
        card,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
        slug=slug
         )
    share_form = ShareForm()
    if request.method == 'POST':
        share_form = ShareForm(request.POST)
        if share_form.is_valid():
            cd = share_form.cleaned_data
            sub = cd['subject']
            email = cd['email']
            link = f"http://{request.get_host()}{post.get_absolute_url()}"
            message = cd['message'] + "\n" + link
            send_mail(sub, message , 'theashkan11@gmail.com', [email])
            messages.success(request, f'An email sent to {email}')
            return redirect("post:post_view",
            year = post.published_at.year,
            month = post.published_at.month,
            day = post.published_at.day,
            slug = post.slug,)
     

    context = {'share_form' : share_form , 'post' : post}
    return render(request, 'posts/Pages/share_email.html',context)

