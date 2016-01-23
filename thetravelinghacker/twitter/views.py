import tweepy
try: import simplejson as json
except ImportError: import json

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response

from thetravelinghacker import settings
from . import Tweet, TwitterUser
from . import serializers


class TwitterUserViewSet(viewsets.ViewSet):
    serializer_class = serializers.TwitterUserSerializer

    def list(self, request):
        twitter_user = search_handle(request)
        serializer = serializers.TwitterUserSerializer(
            instance=twitter_user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            twitter_user = search_handle(pk)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.TwitterUserSerializer(instance=twitter_user)
        return Response(serializer.data)

def home(request):
    """
    Enters the Twitter Angular app
    Renders the Twitter template
    """
    return render_to_response('twitter.html')

def authentify_twitter():
    """
    Initializes the Twitter api
    Returns an api object to make calls to Twitter's api
    """
    auth = tweepy.OAuthHandler(settings.TWITTER_API_CONSUMER_KEY, settings.TWITTER_API_CONSUMER_SECRET)
    auth.set_access_token(settings.TWITTER_API_ACCESS_TOKEN, settings.TWITTER_API_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api

@csrf_exempt
def search_handle(handle):
    """
    Filters data from Twitter api
    Takes an Twitter handle as an argument
    Returns a user and its tweets
    """
    twitter_api = authentify_twitter()

    user = twitter_api.get_user(handle)
    tweets = twitter_api.user_timeline(user.id, count=10)

    user_reputation = calculate_reputation(user)

    new_tweets = []

    for tweet in tweets:
        new_tweets.append(Tweet(
            date=tweet.created_at,
            retweets_count=tweet.retweet_count,
            text=tweet.text,
            photo=get_photo(tweet),
        ))

    new_user = TwitterUser(
        name=user.name,
        screen_name=user.screen_name,
        description=user.description,
        avatar=user.profile_image_url,
        followers_count=user.followers_count,
        followings_count=user.friends_count,
        url=user.url,
        reputation=user_reputation,
        tweets=new_tweets,
    )
    return new_user
    # return HttpResponse(json.dumps(response))

def get_photo(tweet):
    """
    Gets a Tweet's photo, if it is there
    Takes as Tweet as parameter
    Returns a photo url
    """
    try:
        return tweet.entities.get('media', {})[0].get('media_url')
    except KeyError:
        return ''

def calculate_reputation(user):
    """
    Calculates a Twitter account reputation
    Takes a Twitter user as parameter
    Returns a reputation score (max 650)
    """
    # TODO: Reputation algorithm
    return 100

