from django.db import models

# Create your models here.
from uuid import uuid4
from django.db import models
from DjangoUeditor.models import UEditorField


class Article(models.Model):
    """ 文章"""
    uuid = models.UUIDField(default=uuid4)
    title = models.CharField("标题", max_length=15)
    category = models.CharField("分类", max_length=8)
    hint_count = models.IntegerField("点击数", default=0)
    background_img = models.ImageField(upload_to='images/bg_img/', blank=True)
    abstract = models.TextField("摘要", blank=True)
    content = UEditorField(verbose_name=u"内容", imagePath="images/article/", width=1000, height=300, toolbars="full",
                           filePath="files/", default='')
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
