from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import ArticleForm
from .models import Article
from django.views import generic
# Create your views here.

class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/index.html'


class ArticleListView(generic.ListView):
    context_object_name = 'object'
    queryset = Article.objects.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'obj'


class ArticleUpdateView(generic.UpdateView):
    model = Article 
    form_class = ArticleForm
    template_name = 'blog/index.html'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(generic.DeleteView):
    template_name = 'blog/article_delete.html'
    model = Article
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article_list')