from PIL import Image, ImageFilter
import math
import noise
import numpy as np
import random
import sys
import json
import palet

def addTrees(img, x, y, treeCounter):

    pixels = img.load()
    isValid = True

    x = x - 1
    y = y - 1

    if treeCounter % 30 == 0:

        for i in range(2):
            for j in range(4):
                if pixels[x + i, y + j] != palet.dayLand:
                    isValid = False

            x = x + 1
            y = y + 1

            if isValid:

                pixels[x, y] = palet.wood
                pixels[x, y+1] = palet.wood
                pixels[x, y+2] = palet.wood
                pixels[x, y+3] = palet.wood
                pixels[x, y+4] = palet.wood
                pixels[x, y+5] = palet.wood
                pixels[x, y+6] = palet.wood
                pixels[x+2, y+2] = palet.wood
                pixels[x-2, y+2] = palet.wood
                pixels[x+1, y+3] = palet.wood
                pixels[x-1, y+3] = palet.wood

                pixels[x+1, y+1] = palet.leaves
                pixels[x+2, y+1] = palet.leaves
                pixels[x+3, y+1] = palet.leaves
                pixels[x-1, y+1] = palet.leaves
                pixels[x-2, y+1] = palet.leaves
                pixels[x-3, y+1] = palet.leaves
                pixels[x+1, y] = palet.leaves
                pixels[x+2, y] = palet.leaves
                pixels[x-1, y] = palet.leaves
                pixels[x-2, y] = palet.leaves
                pixels[x, y-1] = palet.leaves
                pixels[x+1, y-1] = palet.leaves
                pixels[x+2, y-1] = palet.leaves
                pixels[x-1, y-1] = palet.leaves
                pixels[x-2, y-1] = palet.leaves
                pixels[x, y-2] = palet.leaves
                pixels[x+1, y-2] = palet.leaves
                pixels[x-1, y-2] = palet.leaves

def create_line(segment_length):
    slope = random.randint(1, 6)
    points = []

    # Slope = 0
    if slope == 1:
        for i in range(int(segment_length)):
            points.append([i,0])

    # Slope = 1
    elif slope == 2:
        for i in range(int(segment_length)):
            points.append([i,i])

    # Slope = -1
    elif slope == 3:
        for i in range(int(segment_length)):
            points.append([i,-i])

    # Slope = 2
    elif slope == 4:
        for i in range(int(segment_length)):
            points.append([i,i*2])

    # Slope = -2
    elif slope == 5:
        for i in range(int(segment_length)):
            points.append([i,i*-2])

    # Slope = infinity
    elif slope == 6:
        for i in range(int(segment_length)):
            points.append([0,i])

    return points

def addPaths(img, size, x, y, pathCounter):
    pixels = img.load()
    isValid = True

    black = (0, 0, 0)
    path_length = size / 10
    segment_length = path_length / 10

    if pathCounter % (15) == 0:

        new_x = None
        new_y = None
        x_offset = None
        y_offset = None

        if isValid:

            cur_x = x
            cur_y = y
            for i in range(10):

                #Return the slope points of the segment of the path
                segment = create_line(path_length)

                #Assign these points the color black and then move the starting point
                for p in segment:
                    x_offset = p[0]
                    y_offset = p[1]
                    new_x = cur_x + x_offset
                    new_y = cur_y + y_offset

                    if abs(new_x) < size and abs(new_y) < size:
                        pixels[new_x, new_y] = black
                    cur_x = new_x
                    cur_y = new_y


def checkUserCreatedSeed(user_seed):
    if user_seed[-1] == "_" and user_seed[-2] == "_" and user_seed[-3] == "_" and user_seed[-4] == "_" and user_seed[-4] == "_":
        return False
    return True

def globeMask(img, size):

    Y = np.linspace(-1, 1, size)[None, :]*255
    X = np.linspace(-1, 1, size)[:, None]*255
    alpha = np.sqrt(X**2 + Y**2)
    alpha = 255 - np.clip(0,255,alpha)

    # Push that radial gradient transparency onto red image and save
    img.putalpha(Image.fromarray(alpha.astype(np.uint8)))
    return img
