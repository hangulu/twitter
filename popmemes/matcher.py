"""
This module checks to see if images are similar to each other, using OpenCV.

The tutorial can be found here:
https://www.kaggle.com/wesamelshamy/tutorial-image-feature-extraction-and-matching
"""

import numpy as np
import pandas as pd
import cv2

import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import os

dataset_path = '../popmemes/downloads'

def feature_detection(meme_name):
    """
    Detect and draw the key features in an image.

    meme_name (string): the name of the image
    """
    # Import the meme
    meme = cv2.imread(os.path.join(dataset_path, meme_name))
    # Convert from cv's BRG default color order to RGB
    meme = cv2.cvtColor(meme, cv2.COLOR_BGR2RGB)

    # OpenCV 3 backward incompatibility: Do not create a detector with `cv2.ORB()`.
    orb = cv2.ORB_create()

    # Extract the key points of the photo
    key_points, description = orb.detectAndCompute(meme, None)
    img_keypoints = cv2.drawKeypoints(meme,
                                      key_points,
                                      meme,
                                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Draw circles.
    plt.figure(figsize=(16, 16))
    plt.title('ORB Interest Points')
    plt.imshow(img_keypoints); plt.show()

# Feature matching
# Extract the same features from a different, but similar picture

def image_detect_and_compute(detector, img_name):
    """
    Detect and compute interest points and their descriptors.

    detector: detector object
    img_name (string): name of the image
    return: a triple of the image, key points, and description
    """
    img = cv2.imread(os.path.join(dataset_path, img_name))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = detector.detectAndCompute(img, None)
    return img, kp, des


def draw_image_matches(detector, img1_name, img2_name, nmatches=1):
    """
    Draw ORB feature matches of the given two images.

    detector: detector object
    img1_name (string): name of the first image
    img2_name (string): name of the second image
    matches (int): number of matches to make
    """
    img1, kp1, des1 = image_detect_and_compute(detector, img1_name)
    img2, kp2, des2 = image_detect_and_compute(detector, img2_name)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    # Sort matches by distance - best come first
    matches = sorted(matches, key = lambda x: x.distance)

    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, img2, flags=2)
    plt.figure(figsize=(16, 16))
    plt.title(type(detector))
    plt.imshow(img_matches); plt.show()


def check_similarity(detector, img1_name, img2_name, nmatches=1):
    """
    Check how similar two images are.

    detector: detector object
    img1_name (string): name of the first image
    img2_name (string): name of the second image
    matches (int): number of matches to make
    return: similarity, the number of key points matches out of the total
    number of key points in each image
    """
    img1, kp1, des1 = image_detect_and_compute(detector, img1_name)
    img2, kp2, des2 = image_detect_and_compute(detector, img2_name)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, img2, flags=2)

    # Define similarity as the number of key points matched out of the total
    # number of key points in each image
    similarity = len(matches) / (len(kp1) + len(kp2))

    # Define a threshold of similarity from empirical testing (two Pikachu
    # memes): 42 / 217 ~ 19%
    if similarity > 0.17:
        print(f"{img1_name} and {img2_name} are a match, with a similarity of {str(similarity)}.")
    else:
        print(f"{img1_name} and {img2_name} are not a match, with a similarity of {str(similarity)}.")
    return similarity
