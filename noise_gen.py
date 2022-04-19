from webbrowser import BackgroundBrowser
from PIL import Image, ImageFilter
import noise
import numpy as np
import random
import sys
import json

# Map Color Palets for Day / Night Versions
dayWater = (65,105,225)
nightWater = (0, 0, 51)

dayBeach = (238, 214, 175)
nightBeach = (51, 25, 0)

dayLand = (34,139,34)
nightLand = (0, 51, 0)

dayMountain = (139, 137, 137)
nightMountain = (50, 50, 50)

daySnow = (255, 255, 255)
nightSnow = (105, 105, 105)

wood = (140, 98, 56)
leaves = (140, 198, 62)

def addTrees(img, x, y, treeCounter):

    pixels = img.load()
    isValid = True

    x = x - 1
    y = y - 1

    if treeCounter % 30 == 0:

        for i in range(2):
            for j in range(4):
                if pixels[x + i, y + j] != dayLand:
                    isValid = False

            x = x + 1
            y = y + 1

            if isValid:

                pixels[x, y] = wood
                pixels[x, y+1] = wood
                pixels[x, y+2] = wood
                pixels[x, y+3] = wood
                pixels[x, y+4] = wood
                pixels[x, y+5] = wood
                pixels[x, y+6] = wood
                pixels[x+2, y+2] = wood
                pixels[x-2, y+2] = wood
                pixels[x+1, y+3] = wood
                pixels[x-1, y+3] = wood

                pixels[x+1, y+1] = leaves
                pixels[x+2, y+1] = leaves
                pixels[x+3, y+1] = leaves
                pixels[x-1, y+1] = leaves
                pixels[x-2, y+1] = leaves
                pixels[x-3, y+1] = leaves
                pixels[x+1, y] = leaves
                pixels[x+2, y] = leaves
                pixels[x-1, y] = leaves
                pixels[x-2, y] = leaves
                pixels[x, y-1] = leaves
                pixels[x+1, y-1] = leaves
                pixels[x+2, y-1] = leaves
                pixels[x-1, y-1] = leaves
                pixels[x-2, y-1] = leaves
                pixels[x, y-2] = leaves
                pixels[x+1, y-2] = leaves
                pixels[x-1, y-2] = leaves

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


def create_parabola(segment_length):
    function_choice = random.randint(1, 3)

def create_transcendental(segment_length):
    function_choice = random.randint(1, 3)

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

if __name__ == "__main__":

    seed = None                  # Main value used to randomize overall
    size = None                  # Square size (pixel X pixel)
    day = None                   # Day / Night Color Palet 
    scale = None                 # Level of zoom onto map
    octaves = None               # Level of overall detail
    persistence = None           # Adjusts frequency
    lacunarity = None            # Adjusts amplitude
    trees = None                 # Toggle for including Trees or not
    paths = None                 # Toogle for including Paths or not

    #json file
    settingsFile = sys.argv[1]

    with open(settingsFile, 'r') as f:
        data = json.load(f)

    
    size = int(data["size"])
    scale = float(data["scale"])
    octaves = int(data["octaves"])
    persistence = float(data["persistence"])
    lacunarity = float(data["lacunarity"])
    day = int(data["day"])
    trees = int(data["trees"])
    paths = int(data["paths"]) # Placeholder for paths later on
    user_seed = str(data["seed"])

    # Debug Statements
    print("Size: ",size)
    print("Scale: ", scale)
    print("Octaves: ", octaves)
    print("Persistence:", persistence)
    print("Lacunarity: ", lacunarity)
    print("Day: ", day)
    print("Trees: ", trees)
    print("Paths: ", paths) # Placeholder for paths later on
    print("User Input Seed: ", user_seed)


    f.close()

    # The noise function (snoise2) does not randomize without this value!
    # The option for the user to choose this value will come later
    computer_seed = random.random()
    print("Computer Seed: ", computer_seed)

    # Check if the seed is computer generated or was entered by the user
    if checkUserCreatedSeed(user_seed) == False:
        final_seed = computer_seed
    else:
        final_seed = hash(user_seed) * pow(10, -18)

    

    #Create a new blank image and save the pixels
    img  = Image.new( mode = "RGB", size = (int(size), int(size)), color = (0, 0, 0) )
    pixels = img.load()

    treeCounter = 0
    pathCounter = 0

    # Using the snoise2 function and sliders above, generate the pixel height map values
    for i in range(int(size)):
        for j in range(int(size)):

            #Range is -0.5 <= x <= 0.5 floating point value
            noiseValue = noise.snoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=size, repeaty=size, base=final_seed)
            
            # Based on the value generate and color the pixel accordingly
            if noiseValue < -0.0275:
                if day == 1:
                    pixels[i, j] = dayWater
                else:
                    pixels[i, j] = nightWater
            elif noiseValue < 0:
                if day == 1:
                    pixels[i, j] = dayBeach
                else:
                    pixels[i, j] = nightBeach
            elif noiseValue < 0.3:
                if day == 1:
                    pixels[i, j] = dayLand
                    if i + 3 < size and i - 3 > 0 and j + 3 < size and j - 3 > 0 and paths == 1:
                        addPaths(img, size, i, j, pathCounter)
                        pathCounter += 1
                    if i + 3 < size and i - 3 > 0 and j + 7 < size and j - 7 > 0 and trees == 1:
                        addTrees(img, i, j, treeCounter)
                        treeCounter += 1
                else:
                    pixels[i, j] = nightLand
            elif noiseValue < 0.5:
                if day == 1:
                    pixels[i, j] = dayMountain
                else:
                    pixels[i, j] = nightMountain
            else:
                if day == 1:
                    pixels[i, j] = daySnow
                else:
                    pixels[i, j] = nightSnow

    #View the Image
    img.save("new_map.png", "PNG")  
    img.show()