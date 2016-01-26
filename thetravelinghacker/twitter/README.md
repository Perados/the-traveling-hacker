# Twitter Reputation app

For this project, the tools I used were:
	- Python 3.4.3
	- Django 1.8.4
	- Django REST Framework 3.3.2 
	- AngularJS 1.4.9
	- Tweepy 3.2.0

## The frontend

I used AngularJS, HTML/CSS and Bootstrap for the frontend. Nothing too fancy, just an average single-page app. The interesting part about it is that it is integrated into a Django website, which was not very easy to do, but extremely rewarding experience. I was already planning on migrating the frontend of my personal website to Angular, and now I am convinced. Obviously, the frontend and the Django api are completely independent one from each other. An interesting lesson I learnt while working on this project is that it is not always a good practice to use existing templates or seeds. I used Angular-seed for the Angular app, and that is why it is a bit messy. I also used an HTML/CSS nightmare-template for displaying th Tweets' panels at the beginning, which I ended up replacing with clean Bootstrap.	

## Using Twitter's api

Nowadays, every api needs to implement a secure authentication protocol. The most common ones are OAuth1 and OAuth2, Twitter uses both OAuth1 and OAuth2. The technologies themselves are very interesting, but it takes time to write code to talk to these apis from scratch, and we do not want to reinvent the wheel, there are open source tools out there which do an excellent job talking to Twitter's api. For this project, I used the most popular one for Python: Tweepy (http://docs.tweepy.org/). With Tweepy, you can start using Twitter's api in less than 10 minutes.


## The Django REST api

The Django REST Framework allows us to build RESTful apis in minutes. In this case, it is a very simple one: a single entry point, a single parameter, no authentication required, only GET requests. The user sends a Twitter handle (username) and the api responds with filtered information about that user from Twitter's api. The key part of the api is the "Reputation algorithm": the api gives Reputation points (650 max) to the user, based on his number of followers, his followers' scores and the content of his Tweets.


## The Reputation algorithm: an influence score (650 points max)

There are three cases:

### The user has 200 or less followers (200 points max)

In this case, the user's reputation score will depend on how many of his followers have more than 200 followers. For each follower with more than 200 followers, the users earns 1 point. Which means he can get a maximum of 200 points.

points1 = n where n is the number of the user's followers with more than 200 followers. 

### The user has between 201 and 5000 followers (600 points max)

This kind of user gets automatically the 200 points from the previous category.
The rest of the points are gotten from the amount of followers the user has. If he has 4800 followers plus the 200 from the previous category, then he gets 400 more points. From that, we can calculate the general case:

points2 = (400 * number_of_followers) / 4800  


### The user has more than 1000000 followers (650 points max)

This kind of user gets automatically the 200 points from the first category and the 400 points from the second category.
The 50 extra points he can get are based on the content of the user's Tweets. I used two files to measure if the content of a user is positive or negative. The positive file (https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/positive-words.txt) contains positive words, and the negative file (https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/negative-words.txt) contains negative words. We calculate the total of positive and negative words in the user's last 10 Tweets and we apply the following formula:

points3 = (50 * (positive_words_count-negative_words_count)) / (positive_words_count-negative_words) if positive_words_count != negative_words_count. Otherwise, the user gets 0 points.

The user can get the extra 50 points only if there are only positive words in his last 10 Tweets. 

It is a very simple algorithm, nothing compared to the TunkRank score (http://thenoisychannel.com/2009/01/13/a-twitter-analog-to-pagerank) which I tried to implement without much success. However, I was very surprised by how accurate my algorithm is. For instance, I only got a score of 28, which makes total sense, since I am not influential at all on Twitter, where I only have 66 followers as of 2016/01/26. I also tested my algorithm on the most influential people on Twitter: Katy Perry got a score of 583, Justin Bieber got 633 (I guess he got 33/50 on the last category because his tweets are always very pohsy). CNN got a score of 592, and I would be very surprised to see its score above 600, because most of the news contain negative words. Trump got a score of 650! Politicians, anybody?

curl http://thetravelinghacker.io/api/twitter-users/dmoraces/
curl http://thetravelinghacker.io/api/twitter-users/katyperry/
curl http://thetravelinghacker.io/api/twitter-users/justinbieber/
curl http://thetravelinghacker.io/api/twitter-users/CNN/
curl http://thetravelinghacker.io/api/twitter-users/realDonaldTrump/
