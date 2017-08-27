from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from blog.models import Article, Comments
from blog.forms import CommentForm

# Create your views here.
def home(request):
	articles = Article.objects.all()
	context = {'articles':articles}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html')


def show_article(request, article_id):
	comment_form = CommentForm
	args = {}
	args.update(csrf(request))
	args['article'] = get_object_or_404(Article, id = article_id)
	args['comments'] = Comments.objects.filter(comments_article_id = article_id)
	args['form'] = comment_form
	return render(request, 'blog/article.html', args)

  

	# article = get_object_or_404(Article, id=article_id)
	# args = {'article' : article, 
	# 		'comments' : Comments.objects.filter(comments_article_id = article_id), }
	# return render(request, 'blog/article.html', args)


def addcomment(request, article_id):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save()
			comment.comment_article = Article.objects.get(id = article_id)
			form.save()

	return redirect('article/get/%s/' % article_id)