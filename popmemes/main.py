"""
This module downloads all the pictures from a timeline and compares them to
each other to find the most popular one.
"""

import tweepy
import wget
import cv2
import itertools
from collections import Counter
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
pop_images = []

for img1, img2 in pairs:
    sim = matcher.check_similarity(orb, img1, img2)
    sim_matrix[img1 + " vs. " + img2] = sim
    if sim > 0.18:
        same_images[img1 + " vs. " + img2] = sim
        pop_images.extend([img1, img2])

# Count occurrences of images
occurrences = Counter(pop_images)

# Extract the most popular image
max_image = None
max_occurrence = 0
for im, oc in occurrences.items():
    if (max_image is None) or (oc > max_occurrence):
        max_image = im
        max_occurrence = oc

print(same_images)
if same_images:
    print(f"The most popular meme is {max_image}, which occurred {(max_occurrence / len(pop_images)) * 100} percent of the time.")
else:
    print(f"All the images are unique.")
