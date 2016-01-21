import tweepy
try: import simplejson as json
except ImportError: import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from thetravelinghacker import settings


def home(request):
    """
    Enters the Twitter Angular app
    Takes an http request as an argument
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
def search_handle(request):
    """
    Filters data from Twitter api
    Takes an http request as an argument
    Returns a user and its tweets
    """
    twitter_api = authentify_twitter()

    if request.method == 'GET':
        user = twitter_api.get_user(request.GET.get('handle'))
        tweets = twitter_api.user_timeline(user.id, count=10)

        new_user = {
            "name": user.name,
            "screen_name": user.screen_name,
            "description": user.name,
            "avatar": user.profile_image_url,
            "tweets": user.statuses_count,
            "followers": user.followers_count,
            "following": user.friends_count,
            "url": user.url,
        }
        new_tweets = []

        for tweet in tweets:
            new_tweets.append({"text": tweet.text, "retweets": tweet.retweet_count})

        response = {"user": new_user, "tweets": new_tweets}

        return HttpResponse(json.dumps(response))
