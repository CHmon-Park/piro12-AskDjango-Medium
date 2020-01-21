from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

from django.contrib.auth.decorators import login_required

@login_required()
def post_new(request):
    pass