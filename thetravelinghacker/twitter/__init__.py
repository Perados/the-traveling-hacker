class Tweet(object):
    def __init__(self, **kwargs):
        for field in (
            'date',
            'html_content',
            'id',
            'photo',
            'retweets_count',
            'text',
        ):
            setattr(self, field, kwargs.get(field, None))


class TwitterUser(object):
    def __init__(self, **kwargs):
        for field in (
            'avatar',
            'description',
            'followers_count',
            'followings_count',
            'name',
            'recent_tweets',
            'reputation',
            'screen_name',
            'tweets_count',
            'url',
        ):
            setattr(self, field, kwargs.get(field, None))
