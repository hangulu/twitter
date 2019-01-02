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

# Extract the local features of the Pikachu meme

dataset_path = '../popmemes/test_memes'
# Import the Pikachu meme
pika_1 = cv2.imread(os.path.join(dataset_path, 'pikachu_1.png'))
# Convert from cv's BRG default color order to RGB
pika_1 = cv2.cvtColor(pika_1, cv2.COLOR_BGR2RGB)

# OpenCV 3 backward incompatibility: Do not create a detector with `cv2.ORB()`.
orb = cv2.ORB_create()

# Extract the key points of the photo
key_points, description = orb.detectAndCompute(pika_1, None)
img_keypoints = cv2.drawKeypoints(pika_1,
                                  key_points,
                                  pika_1,
                                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Draw circles.
plt.figure(figsize=(16, 16))
plt.title('ORB Interest Points')
plt.imshow(img_keypoints); plt.show()
