"""
This module downloads all the pictures from a timeline and compares them to
each other to find the most popular one.
"""

import tweepy
import wget
import cv2
import itertools
import matcher
import tl_handler

# Import OAuthHandler parameters
from auth import *

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# ORB creation
orb = cv2.ORB_create()

# Download the latest images from the timeline
num_images = tl_handler.get_and_download(api, '/Users/hakeemangulu/Code/twitter/popmemes/downloads', num_tweets=100)

# Build a list of image names, then their pairwise combinations
names = ["test_img" + str(i) + ".jpg" for i in range(1, num_images)]
pairs = list(itertools.combinations(names, 2))

# Build the similarity matrix
sim_matrix = dict()
same_images = dict()
for img1, img2 in pairs:
    sim = matcher.check_similarity(orb, img1, img2)
    sim_matrix[img1 + " vs. " + img2] = sim
    if sim > 0.18:
        same_images[img1 + " vs. " + img2] = sim

print(same_images)
