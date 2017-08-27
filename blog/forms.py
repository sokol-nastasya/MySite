from django import forms
from django.contrib.auth import models
from django.forms import ModelForm
from blog.models import Article, Comments

class CommentForm(ModelForm):

	class Meta:
		model = Comments
		fields = ('comments_text', )

	

