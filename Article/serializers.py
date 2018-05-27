#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils.safestring import mark_safe
from Article.models import Article


def strftimeYMD(time):
    return time.strftime("%Y-%m-%d")


class ArticleSer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()

    def get_create_time(self, obj):
        return strftimeYMD(obj.create_time)

    class Meta:
        model = Article
        fields = ('uuid', 'create_time', 'category',
                  'hint_count', 'abstract', 'background_img')


class ArticleDetailSer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_create_time(self, obj):
        return strftimeYMD(obj.create_time)

    def get_content(self, obj):
        return mark_safe(obj.content)

    class Meta:
        model = Article
        fields = ('uuid', 'create_time', 'category', 'title',
                  'content', 'background_img')
