from django.shortcuts import render,get_object_or_404,HttpResponseRedirect

# Create your views here.
from django.views.generic.list import ListView
from blog.models import Article, Category,Archives,BlogComment,Tag
from .forms import BlogCommentForm
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.edit import FormView


class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p').order_by('created_time')[:5]
        f = 0
        n = -1
        for article in article_list:
            if len(article.abstract)==0:
                article.abstract = str(article.body)[:100]
            # if f==0:
            #     if article.topped==True:
            #         article_copy = article
            #         f = 1
            #     n +=1
            # else:
            #     article.topped = False
                article.save()
        #del article_list[n]
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')[:3]
        kwargs['recent_post_list'] = Article.objects.filter(status='p').order_by('last_modified_time')[:3]
        kwargs['archives_list']  = Archives.objects.all().order_by('created_time')[:3]
        kwargs['tag_list'] = Tag.objects.all().order_by('created_time')[:3]
        return super(IndexView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'
    obj = Article()

    def get_object(self, queryset=None):
        self.obj = super(ArticleDetailView, self).get_object()
        self.obj.views +=1
        self.obj.save()
        return self.obj

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')[:3]
        kwargs['recent_post_list']=Article.objects.filter(status='p').order_by('last_modified_time')[:3]
        kwargs['archives_list'] = Archives.objects.all().order_by('created_time')[:3]
        kwargs['tag_list'] = Tag.objects.all().order_by('created_time')[:3]
        kwargs['in_tag_list'] = self.obj.tag.all()
        kwargs['comment_list'] = self.object.blogcomment_set.all()
        kwargs['form'] = BlogCommentForm()
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class IncategoryView(ListView):
    template_name = "blog/in-category.html"
    context_object_name = "contacts"

    def get_queryset(self):
        in_category_list = Article.objects.filter(category=self.kwargs['category_id'],status='p')
        for article in in_category_list:
            if len(article.abstract)==0:
                article.abstract = str(article.body)[:100]
                article.save()
        page = self.kwargs['pagenumber']
        paginator = Paginator(in_category_list, 4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')[:3]
        kwargs['recent_post_list']=Article.objects.filter(status='p').order_by('last_modified_time')[:3]
        kwargs['archives_list'] = Archives.objects.all().order_by('created_time')[:3]
        kwargs['tag_list'] = Tag.objects.all().order_by('created_time')[:3]
        kwargs['in_category_list'] = self.contacts
        return super(IncategoryView, self).get_context_data(**kwargs)


class InarchivesView(ListView):
    template_name = "blog/in-archives.html"
    context_object_name = "contacts"

    def get_queryset(self):
        in_archives_list = Article.objects.filter(archives=self.kwargs['archives_id'],status='p')
        for article in in_archives_list:
            if len(article.abstract)==0:
                article.abstract = str(article.body)[:100]
                article.save()
        page = self.kwargs['pagenumber']
        paginator = Paginator(in_archives_list, 4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')[:3]
        kwargs['recent_post_list']=Article.objects.filter(status='p').order_by('last_modified_time')[:3]
        kwargs['archives_list'] = Archives.objects.all().order_by('created_time')[:3]
        kwargs['tag_list'] = Tag.objects.all().order_by('created_time')[:3]
        kwargs['in_archives_list'] = self.contacts
        return super(InarchivesView, self).get_context_data(**kwargs)


class IntagView(ListView):
    template_name = "blog/in-tag.html"
    context_object_name = "contacts"

    def get_queryset(self):
        in_tag_list = Article.objects.filter(tag=self.kwargs['tag_id'], status='p')
        for article in in_tag_list:
            if len(article.abstract) == 0:
                article.abstract = str(article.body)[:100]
                article.save()
        page = self.kwargs['pagenumber']
        paginator = Paginator(in_tag_list,4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')[:3]
        kwargs['recent_post_list'] = Article.objects.filter(status='p').order_by('last_modified_time')[:3]
        kwargs['archives_list'] = Archives.objects.all().order_by('created_time')[:3]
        kwargs['tag_list'] = Tag.objects.all().order_by('created_time')[:3]
        kwargs['in_tag_list'] = self.contacts
        kwargs['tag_id'] = self.kwargs['tag_id']
        return super(IntagView, self).get_context_data(**kwargs)

class PageListOfArticle(ListView):
    template_name = 'blog/page-of-article.html'
    context_object_name = 'contacts'
    contact = []

    def get_queryset(self):
        page = self.kwargs['pagenumber']
        article_lists = Article.objects.all()
        paginator = Paginator(article_lists, 4)
        self.contact = paginator.page(page)
        return self.contact

    def get_context_data(self, **kwargs):
        kwargs['article_list'] = self.contact
        return super(PageListOfArticle, self).get_context_data(**kwargs)

class PageListOfArchives(ListView):
    template_name = 'blog/page-of-archives.html'
    context_object_name = 'contacts'
    contact = []

    def get_queryset(self):
        page = self.kwargs['pagenumber']
        article_lists = Archives.objects.all()
        paginator = Paginator(article_lists, 4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['archives_list'] = self.contacts
        return super(PageListOfArchives, self).get_context_data(**kwargs)

class PageListOfCategory(ListView):
    template_name = 'blog/page-of-category.html'
    context_object_name = 'contacts'
    contact = []

    def get_queryset(self):
        page = self.kwargs['pagenumber']
        article_lists = Category.objects.all()
        paginator = Paginator(article_lists, 4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = self.contacts
        return super(PageListOfCategory, self).get_context_data(**kwargs)

class PageListOfTag(ListView):
    template_name = 'blog/page-of-tag.html'
    context_object_name = 'contacts'
    contact = []

    def get_queryset(self):
        page = self.kwargs['pagenumber']
        tag_lists = Tag.objects.all()
        paginator = Paginator(tag_lists, 4)
        self.contacts = paginator.page(page)
        return self.contacts

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = self.contacts
        return super(PageListOfTag, self).get_context_data(**kwargs)

class CommentPostView(FormView):
    form_class = BlogCommentForm
    template_name = 'blog/detail.html'

    def form_valid(self, form):
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        comment = form.save(commit=False)
        comment.article = target_article
        comment.save()

        self.success_url = target_article.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])

        return render(self.request, 'blog/detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.blogcomment_set.all(),
        })



class About(ListView):
    template_name = "blog/about.html"
    def get_queryset(self):
        pass

class Contact(ListView):
    template_name = "blog/contact.html"
    def get_queryset(self):
        pass
