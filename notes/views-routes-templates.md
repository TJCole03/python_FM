Views and routes: 
    Allows mapping to URLs in web apps to pages, apis, points, etc.

<!-- EXPAND DROPDOWN ARROWS FOR FULL NOTES ON BASE.HTML -->

<!-- base tempalte that all other templates use -->
{% load static %} --> "load up all the static resources we might need"

<html>
<head>
                                                    <!--{% %} are template tags; allow use of special commands in HTML templates that let them interfacei with django  -->
    <link rel="stylesheet" type="text/css" href="{% static 'blog/css/blog.css' %}">
</head>

<body>
    <header class="o-box c-site-header">
        <nav class="o-max-width c-site-nav">
            <a class="c-site-nav__link c-site-nav__wordmark" href="/">My Python Blog</a>
            <ul class="u-no-margin u-no-padding c-site-nav__list">
                <li class="c-site-nav__item"><a class="c-site-nav__link" href="{% url 'about' %}">About</a></li>
            </ul>
        </nav>
    </header>

    <main class="o-max-width o-site-main">

    <!-- Content blocks let us use base.html as a template. -->
    {% block content %}
    {% endblock %}
    </main>

    <footer class="o-box c-site-footer">
        <div class="o-max-width">
            <p>The <a href="https://practical.learnpython.dev">Practical Python Blog</a>, built with Django!</p>
            <p><em><small>Created for Practical Python</small></em></p>
        </div>
    </footer>
</body>
</html>

<!-- about.html -->
<!-- EVERYTHING BETWEEN THESE CONTENT BLOCKS GETS INSERTED INTO BASE.HTML ON LINES 28/29 
     BETWEEN BLOCK CONTENT AND ENDBLOCK -->
{% extends 'blog/base.html' %}
{% block content %}
<article class="o-box c-card c-post"> 0_0
This is a page with info about the author. 0_0
</article> 0_0
{% endblock %}

<!-- class based views; EXAMPLE DOWN BELOW -->

<!-- URLS.PY -->

from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="posts"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.post, name="post"),
]

<!-- VIEWS.PY -->
<!-- THESE VIEWS MAP TO URLS.PY -->
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from blog.models import Post

<!-- gets a template and renders it! -->
def about(request): 
    template = loader.get_template("blog/about.html")
    return HttpResponse(template.render({}, request))

<!-- takes a post, getting all the objects in db, 
    creating a context, and returning render of blog/post -->
def index(request):
    posts = Post.objects.all()
    context = {"post_list": posts}
    return render(request, "blog/post_list.html", context=context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    return render(request, "blog/post_detail.html", {"post": post})

<!-- FROM CLASS_BASED_VIEWS.PY -->

from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
