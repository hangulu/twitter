"""
This module downloads all the pictures from a timeline.

The tutorial can be found here:
https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
"""

import tweepy
import wget
import os

# Import OAuthHandler parameters
from popmemes.auth import *

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_media(api, num_tweets=25, profile="@hakeemangulu", admin=False):
    """
    Get all the media files from the timeline.

    api (Tweepy API object): The authentiated API access object.
    num_tweets (int): The number of tweets to scan on the timeline.
    profile (string): The Twitter handle of the user to be analyzed.
    admin (boolean): Whether the administrator is using the application.
    return: a set of urls for media
    """
    # Store the media urls in a list
    media_files = []

    # Create cursor object for the timeline
    if admin:
        # If the admin is using the application, return his timeline
        tl = tweepy.Cursor(api.home_timeline).items(num_tweets)
    else:
        # If the admin is not using the application, return the specified
        # user's timeline
        tl = tweepy.Cursor(api.user_timeline, screen_name=profile).items(num_tweets)

    # Iterate through the timeline and extract images
    for status in tl:
        # Get all media from a tweet
        media = status.entities.get('media', [])
        # Add non-empty media to the set
        for image in media:
            # Only add the image if it is a photo or GIF (as opposed to a
            # video)
            if image['type'] == 'photo' or image['type'] == 'animated_gif':
                media_files.append(image['media_url'])
    return media_files

def downloader(urls, path):
    """
    Given a set of urls, downloads the files to a given path.

    urls (set): A set of urls.
    path (string): A local path for storage.
    return: the number of files downloaded
    """
    counter = 1
    for media_file in urls:
        # Create the file name
        file_name = "meme" + str(counter) + ".jpg"
        file_location = path + "/" + file_name
        print(f"Downloading {media_file} as {file_name}.")
        # Overwrite files
        if os.path.exists(file_location):
            os.remove(file_location)
            print(f"{file_name} will overwrite an existing file of the same name.")
        wget.download(media_file, out=file_location)
        print("\n")
        counter += 1
    print(f"{counter - 1} items were downloaded.")
    return counter - 1

def get_and_download(api, path, num_tweets=25, profile="@hakeemangulu", admin=False):
    """
    A combination of the get_media and downloader functions, thus finding
    the media then downloading it in one call.

    api (Tweepy API object): The authentiated API access object.
    num_tweets (int): The number of tweets to scan on the timeline.
    path (string): A local path for storage.
    profile (string): The Twitter handle of the user to be analyzed.
    return: the number of files downloaded
    """
    return downloader(get_media(api, num_tweets, profile, admin), path)
