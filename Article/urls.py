from django.conf.urls import url, include
from Article.views import ArticleListView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="article-list")
]
