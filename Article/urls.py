from django.conf.urls import url, include
from Article.views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="article-list"),
    url('detail/(?P<uuid>[0-9a-zA-Z\-]*)/?$', ArticleDetailView.as_view(), name='article-detail')
]
