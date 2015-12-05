from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
	latest_blog_list = Post.objects.order_by('-pub_date')

	context={
		"blogList": latest_blog_list, 

	}

	return render(request, "index.html", context)