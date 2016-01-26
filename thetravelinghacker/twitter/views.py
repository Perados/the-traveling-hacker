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
        except tweepy.error.TweepError:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "User not found."})
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

def search_handle(handle):
    """
    Filters data from Twitter api
    Takes an Twitter handle as an argument
    Returns a user and its tweets
    """
    twitter_api = authentify_twitter()

    try:
        user = twitter_api.get_user(handle)
    except tweepy.error.TweepError:
        raise

    tweets = twitter_api.user_timeline(user.id, count=10)

    user_reputation = calculate_reputation(user, twitter_api)

    recent_tweets = []

    for tweet in tweets:
        recent_tweets.append(Tweet(
            date=tweet.created_at,
            html_content =twitter_api.get_oembed(tweet.id, hide_media=False).get("html"),
            id=tweet.id,
            photo=get_photo(tweet),
            retweets_count=tweet.retweet_count,
            text=tweet.text,
        ))

    new_user = TwitterUser(
        avatar=user.profile_image_url,
        description=user.description,
        followers_count=user.followers_count,
        followings_count=user.friends_count,
        name=user.name,
        recent_tweets=recent_tweets,
        reputation=user_reputation,
        screen_name=user.screen_name,
        tweets_count=user.statuses_count,
        url=user.url,
    )
    return new_user

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

def calculate_reputation(user, twitter_api):
    """
    Calculates a Twitter account reputation
    Takes a Twitter user as parameter
    Returns a reputation score (max 650)
    """
    followers_count = user.followers_count
    reputation = 0

    if followers_count < 201:
        followers = user.followers(count=200)
        for follower in followers:
            if follower.followers_count > 200:
                reputation +=1
    elif 200 < followers_count < 5001:
        reputation = 200
        reputation += (400 * (followers_count - 200)) / 4800
    else:
        reputation = 600
        reputation += analyze_user(user)

    return reputation

def analyze_user(user):
    """
    Analyzes a user's tweets
    Takes a Twitter user and the twitter_api object as parameters
    Returns a score (max 50)
    """
    with open('thetravelinghacker/static/twitter/positive-words.txt', 'r')  as file:
        positive_words = file.read().splitlines()
    with open('thetravelinghacker/static/twitter/negative-words.txt', 'r')  as file:
        negative_words = file.read().splitlines()

    positive_words_count = 0
    negative_words_count = 0

    user_tweets = user.timeline(count=10, include_rts=1)

    for tweet in user_tweets:

        for word in tweet.text:
            if word in positive_words:
                positive_words_count += 1
            elif word in negative_words:
                negative_words_count += 1
            else:
                pass

    if positive_words_count != negative_words_count:
        points = (50 * (positive_words_count-negative_words_count)) / (positive_words_count)
    else:
        points = 0

    return points

