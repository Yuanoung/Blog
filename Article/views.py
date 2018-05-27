from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from Article.models import Article
from Article.serializers import ArticleSer, ArticleDetailSer


class ArticleListView(ListAPIView):
    serializer_class = ArticleSer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_queryset(self):
        return Article.objects.all().order_by("-create_time", )

    def get(self, request, *args, **kwargs):
        r = super().get(request, *args, **kwargs)
        data = {
            "article_list": r.data["results"],
            "next_url": r.data["next"]
        }
        return Response(data, template_name="home.html", status=200)


class ArticleDetailView(APIView):
    serializer_class = ArticleDetailSer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_other_article(self, create_time):
        other_data = dict()
        before_art = Article.objects.filter(create_time__gt=create_time).first()
        after_art = Article.objects.filter(create_time__lt=create_time).order_by("-create_time").first()

        if after_art:
            after_ser = ArticleSer(after_art)
            other_data["after"] = after_ser.data
        if before_art:
            before_ser = ArticleSer(before_art)
            other_data["before"] = before_ser.data

        return other_data

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(uuid=kwargs["uuid"])
        article.hint_count += 1
        article.save(update_fields=('hint_count',))
        ser_data = ArticleDetailSer(article).data
        other_data = self.get_other_article(article.create_time)
        ser_data.update(other_data)
        return Response(ser_data, template_name="content.html", status=200)
