
# run in command prompt (no output files)
# python OpenCV-yolo-stream.py --yolo yolo-coco --url https://youtu.be/1EiC9bvVGnk

# run in command prompt (with output files)
# python OpenCV-yolo-stream.py --yolo yolo-coco --url https://youtu.be/1EiC9bvVGnk --output output/ouput_videosteam.avi --data output/CSV/data_videosteam.csv 

# JacksonHole streams https://youtu.be/RZWzyQuFxgE & https://youtu.be/1EiC9bvVGnk

# import the necessary packages
import numpy as np
import pandas as pd
import argparse
import time
import datetime
import cv2
import os
import pafy
import streamlink