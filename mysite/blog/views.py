# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http.response import HttpResponse
from blog.models import Post

from rest_framework.generics import GenericAPIView
from rest_framework import serializers, mixins
# Create your views here.
def blog_page(request):
    
    return HttpResponse('Hello!')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
#        fields =('title', 'content', 'reg_date')

class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self):
        return self.list(request, *args, **kwargs)