class Tweet(object):
    def __init__(self, **kwargs):
        for field in (
            'date',
            'retweets_count',
            'text',
            'photo',
        ):
            setattr(self, field, kwargs.get(field, None))


class TwitterUser(object):
    def __init__(self, **kwargs):
        for field in (
                'name',
                'screen_name',
                'description',
                'avatar',
                'followers_count',
                'followings_count',
                'url',
                'reputation',
                'tweets',
        ):
            setattr(self, field, kwargs.get(field, None))
