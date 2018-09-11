from django.shortcuts import render
from rest_framework import viewsets, mixins

from apps.tweets.api.v1.serializers import TweetSerializer
from apps.tweets.models import Tweet


class TweetViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
