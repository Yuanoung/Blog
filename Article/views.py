from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from Article.models import Article
from Article.serializers import ArticleSer


class ArticleListView(ListAPIView):
    serializer_class = ArticleSer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_queryset(self):
        return Article.objects.all().order_by("-create_time", )

    def get(self, request, *args, **kwargs):
        r = super().get(request, *args, **kwargs)
        print(r.data)
        data = {
            "article_list": r.data["results"],
            "next_url": r.data["next"]
        }
        print(data)
        return Response(data, template_name="home.html", status=200)
