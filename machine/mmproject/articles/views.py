from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from articles.models import Article


# Create your views here.


def hello(request):
    name = "Ashvinee"
    html = "<html><body>Hi %s.this seems to have worked!.</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "Ashvinee"
    t = get_template('hello.html')
    html = t.render(Context({'name' : name}))
    return HttpResponse(html)


def hello_template_simple(request):
    name = "Ashvinee"
    return render_to_response('hello.html',{'name': name})


class HelloTemplate(TemplateView):

    template_name = 'helloclass.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate,self).get_context_data(**kwargs)
        context['name'] = 'Ashvinee'
        return context


def home(request):
    return render(
        request,"home.html"
    )


#def articles(request):
 #   return render_to_response('articles.html',
  #                            {'articles':Article.objects.all()})


#def article(request,article_id=1):
 #   return render_to_response('article.html',
  #                            {'article':Article.objects.get(id=article_id)})