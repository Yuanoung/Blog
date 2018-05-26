#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from Article.models import Article


class ArticleSer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('uuid', 'create_time', 'category',
                  'hint_count', 'abstract', 'background_img')
