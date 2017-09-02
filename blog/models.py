from django.db import models
from django.contrib.auth.models import User

SHORT_TEXT_LEN = 1000

class Article(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	likes = models.IntegerField(default = 0)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_short_text(self):
		if len(self.text) > SHORT_TEXT_LEN:
			return self.text[:SHORT_TEXT_LEN]
		else:
			return self.text

class Comments(models.Model):
	comments_text = models.TextField(verbose_name = "Комментарии")
	comments_article = models.ForeignKey(Article)