"""
This module downloads all the pictures from a timeline.

The tutorial can be found here:
https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
"""

import tweepy
import json

# Import OAuthHandler parameters
from auth import *

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Store the media urls in a set
media_files = set()
# Iterate through the timeline and extract images
for status in tweepy.Cursor(api.home_timeline).items(25):
    media = status.entities.get('media', [])
    # Add non-empty media to the set
    if media:
        print(media[0]['media_url'])
        media_files.add(media[0]['media_url'])
