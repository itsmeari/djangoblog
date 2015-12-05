from django.shortcuts import render
from blog.models import Post, Comment

def home (request):
	blog_posts_list = Post.objects.order_by('-pub_date')[:5]
	context = {"blog_posts_list":blog_posts_list}
	#return always last
	return render(request, 'index.html', context)

def detail (request, blog_id):

	blog = Post.objects.get(pk=blog_id)
	comments = blog.comments.all()

	context = {
		"blog_id": blog_id,
		"blog": blog,
		"comments": comments,
	}
	return render(request, 'blog.html', context)

#def about (request):
	#return render (request, 'about.html')