from rest_framework import serializers
from apps.tweets.models import Tweet


class TweetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tweet
        fields = (
            'id',
            'name',
            'content',
            'timestamp',
        )
