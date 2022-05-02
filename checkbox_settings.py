from PIL import Image, ImageFilter
import math
import noise
import numpy as np
import random
import sys
import json
import palet

def addTrees(img, size, x, y, treeCounter):

    # Check if the placement is in bounds
    if x + 3 < size and x - 3 > 0 and y + 7 < size and y - 7 > 0:

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

    if x + 3 < size and x - 3 > 0 and y + 3 < size and y - 3 > 0:
        pixels = img.load()
        isValid = True

        black = (0, 0, 0)
        numTrails = 0
        new_x = None
        new_y = None

        while(numTrails < 25):
            # Choose two random points
            x1 = random.randint(1, size - 1)
            y1 = random.randint(1, size - 1)
            x2 = random.randint(1, size - 1)
            y2 = random.randint(1, size - 1)

            # Check the points don't equal each other
            if x1 == x2 or y1 == y2:
                continue

            # Calculate the difference between points
            run = (x2 - x1)
            rise = (y2 - y1)

            # Assign a moving point for coloring
            new_x = x1
            new_y = y1

            # Only place the paths on grass
            if pixels[x1, y1] == palet.dayLand and pixels[x2, y2] == palet.dayLand:
                placing = True
                pixelsPlaced = False
                while(placing):
                    if new_x == x2 or new_y == y2 or abs(new_x) >= size or abs(new_y) >= size:
                        placing = False
                        continue

                    if pixels[new_x, new_y] != palet.dayWater:
                        # Keep track of if a trail is being placed
                        pixelsPlaced = True
                        pixels[new_x, new_y] = black

                    # Get the next point
                    new_x = new_x + round(run / 100) + 1
                    new_y = new_y + round(rise / 100) + 1

                    # Add some randomnss so the line is not perfectly straight
                    randomness = random.randint(1,100)
                    if randomness < 5:
                        new_x = new_x + 2
                    elif randomness > 6 and randomness < 10:
                        new_y = new_y + 2
                    elif randomness > 11 and randomness < 15:
                        new_x = new_x - 2
                    elif randomness > 16 and randomness < 20:
                        new_y = new_y - 2

                if pixelsPlaced:
                    numTrails = numTrails + 1

        print("Paths done")

def checkUserCreatedSeed(user_seed):
    if user_seed[-1] == "_" and user_seed[-2] == "_" and user_seed[-3] == "_" and user_seed[-4] == "_" and user_seed[-5] == "_":
        return False
    return True

def globeMask(img, size):

    # Ensure scale and ratio of image is maintained 
    Y = np.linspace(-1, 1, size)[None, :] * 255
    X = np.linspace(-1, 1, size)[:, None] * 255

    alpha = np.sqrt(X**2 + Y**2)
    alpha = 255 - np.clip(0,255,alpha)

    # Push that radial gradient transparency onto red image and save
    img.putalpha(Image.fromarray(alpha.astype(np.uint8)))
    return img
