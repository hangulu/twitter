"""
This module downloads all the pictures from a timeline and compares them to
each other to find the most popular one.
"""

import tweepy
import wget
import cv2
import itertools
from collections import Counter
import shutil

import matcher
import tl_handler

# Import OAuthHandler parameters
from auth import *

def memr(username):
    """
    Run the meme finding function.

    username (string): The Twiter handle of the user to be analyzed.
    return: the top meme
    """
    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # ORB creation
    orb = cv2.ORB_create()

    # # Accept the user's handle as input
    # user = "@" + input("Whose timeline would you like to analyze? ")

    user = "@" + username

    if user == "@adminpass":
        print("You've entered the admin password. Now analyzing @hakeemangulu's full timeline. \n")
        num_images = tl_handler.get_and_download(api, '/Users/hakeemangulu/Code/twitter/popmemes/downloads', num_tweets=100, admin=True)
    else:
        print(f"Now analyzing {user}'s timeline for memes.\n")
        # Download the latest images from the timeline
        try:
            num_images = tl_handler.get_and_download(api, '/Users/hakeemangulu/Code/twitter/popmemes/downloads', num_tweets=100, profile=user)
        except ValueError:
            print("We cannot analyze this user's profile. Please re-run the script and try again.")
            return "failure", 0
            # quit()

    # Build a list of image names, then their pairwise combinations
    names = ["meme" + str(i) + ".jpg" for i in range(1, num_images + 1)]
    pairs = list(itertools.combinations(names, 2))

    # Build the similarity matrix
    sim_matrix = dict()
    same_images = dict()
    pop_images = []

    for img1, img2 in pairs:
        sim = matcher.check_similarity(orb, img1, img2)
        sim_matrix[img1 + " vs. " + img2] = sim
        if sim > 0.17:
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
        pop_freq = (float(max_occurrence) / len(sim_matrix)) * 100
        print(f"The most popular meme is {max_image}, which occurred {pop_freq} percent of the time.")
    else:
        pop_freq = 0.
        print(f"All the images are unique.")

    # Copy the file to the src folder
    shutil.copyfile(f'/Users/hakeemangulu/Code/twitter/popmemes/downloads/{max_image}.jpg', f'/Users/hakeemangulu/Code/twitter/popmemes/src/images/popimg.jpg')
    return max_image, pop_freq

if __name__ == '__main__':
    memr()
