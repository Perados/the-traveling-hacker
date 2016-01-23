from rest_framework import serializers
from . import Tweet, TwitterUser


class TweetSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    retweets_count = serializers.IntegerField()
    text = serializers.CharField(max_length=1000)
    photo = serializers.URLField(max_length=1000)

    def create(self, validated_data):
        return Tweet(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class TwitterUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    screen_name = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=1000)
    avatar = serializers.URLField(max_length=1000)
    followers_count = serializers.IntegerField()
    followings_count = serializers.IntegerField()
    url = serializers.URLField(max_length=1000)
    reputation = serializers.IntegerField()
    tweets = TweetSerializer(many=True)

    def create(self, validated_data):
        return TwitterUser(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
