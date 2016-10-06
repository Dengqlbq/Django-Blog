from blog import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/',views.About.as_view(),name='about'),
    url(r'^contact/', views.Contact.as_view(), name='contact'),

    url(r'^article/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='detail'),

    url(r'^incategory/(?P<category_id>\d+)/page/(?P<pagenumber>\d+)$', views.IncategoryView.as_view(), name='in-category'),
    url(r'^inarchives/(?P<archives_id>\d+)/page/(?P<pagenumber>\d+)$', views.InarchivesView.as_view(), name='in-archives'),
    url(r'^intag/(?P<tag_id>\d+)/page/(?P<pagenumber>\d+)', views.IntagView.as_view(), name='in-tag'),

    url(r'^page-of-article/(?P<pagenumber>\d+)', views.PageListOfArticle.as_view(),name='page-of-article'),
    url(r'^page-of-archives/(?P<pagenumber>\d+)', views.PageListOfArchives.as_view(),name='page-of-archives'),
    url(r'^page-of-category/(?P<pagenumber>\d+)', views.PageListOfCategory.as_view(),name='page-of-category'),
    url(r'^page-of-tag/(?P<pagenumber>\d+)', views.PageListOfTag.as_view(),name='page-of-tag'),

    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentPostView.as_view(), name='comment'),
]