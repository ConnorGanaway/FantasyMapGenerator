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

def addTrees(img):

    pixels = img.load()

    #for i in range(int(size)):
    #    for j in range(int(size)):
    print()
    i = 50
    j = 50

    if pixels[i, j] == dayLand:

        pixels[i, j] = wood
        pixels[i, j+1] = wood
        pixels[i, j+2] = wood
        pixels[i, j+3] = wood
        pixels[i, j+4] = wood
        pixels[i, j+5] = wood
        pixels[i, j+6] = wood
        pixels[i+2, j+2] = wood
        pixels[i-2, j+2] = wood
        pixels[i+1, j+3] = wood
        pixels[i-1, j+3] = wood

        pixels[i+1, j+1] = leaves
        pixels[i+2, j+1] = leaves
        pixels[i+3, j+1] = leaves
        pixels[i-1, j+1] = leaves
        pixels[i-2, j+1] = leaves
        pixels[i-3, j+1] = leaves
        pixels[i+1, j] = leaves
        pixels[i+2, j] = leaves
        pixels[i-1, j] = leaves
        pixels[i-2, j] = leaves
        pixels[i, j-1] = leaves
        pixels[i+1, j-1] = leaves
        pixels[i+2, j-1] = leaves
        pixels[i-1, j-1] = leaves
        pixels[i-2, j-1] = leaves
        pixels[i, j-2] = leaves
        pixels[i+1, j-2] = leaves
        pixels[i-1, j-2] = leaves


if __name__ == "__main__":

    seed = None                  # Main value used to randomize overall
    size = None                  # Square size (pixel X pixel)
    day = None                   # Day / Night Color Palet 
    scale = None                 # Level of zoom onto map
    octaves = None               # Level of overall detail
    persistence = None           # Adjusts frequency
    lacunarity = None            # Adjusts amplitude

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
    user_seed = str(data["seed"])

    # Debug Statements
    print("Size: ",size)
    print("Scale: ", scale)
    print("Octaves: ", octaves)
    print("Persistence:", persistence)
    print("Lacunarity: ", lacunarity)
    print("Day: ", day)
    print("User Input Seed: ", user_seed)   #This is a placeholder for later on in the project


    f.close()

    # The noise function (snoise2) does not randomize without this value!
    # The option for the user to choose this value will come later
    computer_seed = random.random()
    print("Computer Seed: ", computer_seed)

    print("hash: ", hash(user_seed))
    final_seed = hash(user_seed) * computer_seed * pow(10, -18)
    print("hash: ", final_seed)

    #Create a new blank image and save the pixels
    img  = Image.new( mode = "RGB", size = (int(size), int(size)), color = (0, 0, 0) )
    pixels = img.load()

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
    addTrees(img)
    img.save("../../../new_map.png", "PNG")  
    img.show()