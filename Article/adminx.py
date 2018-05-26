#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from Article.models import Article


class ArticleAdmin(object):
    list_display = ['title', 'category', 'hint_count', 'content']
    style_fields = {"content": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)
