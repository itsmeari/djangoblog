import datetime

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
	title = models.CharField(max_length = 255)
	pub_date = models.DateTimeField("date published")
	author = models.CharField(max_length = 255)
	blog_text = models.TextField()
	preview_text = models.TextField(blank = True)
	tags = TaggableManager()
	block_quote = models.TextField(blank = True)
	block_source = models.CharField(max_length = 255, blank = True)
	category = models.ForeignKey('blog.Category')

	def __unicode__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now - timedate.timedelta(days = 1)

	was_published_recently.admin_order_field = "pub_date"
	was_published_recently.boolean = True
	was_published_recently.short_description = "published recently?"

class Category(models.Model):
	title = models.CharField(max_length = 100, db_index = True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	post_id = models.ForeignKey(Post, related_name="comments")
	comment_text = models.TextField()
	commenter_name = models.CharField(max_length=60)
	email = models.EmailField(max_length=254)
	time_stamp = models.DateTimeField(auto_now=True)
