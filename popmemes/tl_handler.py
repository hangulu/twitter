"""
This module downloads all the pictures from a timeline.

The tutorial can be found here:
https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
"""

import tweepy
import json
import wget

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
        media_files.add(media[0]['media_url'])

def downloader(urls, path):
    """
    Given a set of urls, downloads the files to a given path.

    urls (set): A set of urls.
    path (string): A local path for storage.
    """
    counter = 1
    for media_file in urls:
        file_name = "test_img" + str(counter) + ".jpg"
        file_location = path + "/" + file_name
        print(f"Downloading {media_file} as {file_name}.")
        wget.download(media_file, out=file_location)
        print("\n")
        counter += 1
    print(f"{counter} items were downloaded.")

downloader(media_files, '/Users/hakeemangulu/Code/twitter/popmemes/downloads')
