# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http.response import HttpResponse
from blog.models import Post

# Create your views here.
def blog_page(request):
    
    return HttpResponse('Hello!')

#def blog_a

