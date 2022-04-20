from PIL import Image, ImageFilter
import math
import noise
import numpy as np
import random
import sys
import json
import palet                # Color Palet definitions
import checkbox_settings    # Functions for the checkboxs on the app

showDebugMessages = True

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
    paths = int(data["paths"])
    mask = int(data["mask"])
    user_seed = str(data["seed"])

    # Debug Statements
    if showDebugMessages == True:
        print("Size: ",size)
        print("Scale: ", scale)
        print("Octaves: ", octaves)
        print("Persistence:", persistence)
        print("Lacunarity: ", lacunarity)
        print("Day: ", day)
        print("Trees: ", trees)
        print("Paths: ", paths)
        print("Mask: ", mask)
        print("User Input Seed: ", user_seed)

    f.close()

    # The noise function (snoise2) does not randomize without this value!
    # The option for the user to choose this value will come later
    computer_seed = random.random()
    print("Computer Seed: ", computer_seed)

    # Check if the seed is computer generated or was entered by the user
    if checkbox_settings.checkUserCreatedSeed(user_seed) == False:
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
                    pixels[i, j] = palet.dayWater
                else:
                    pixels[i, j] = palet.nightWater
            elif noiseValue < 0:
                if day == 1:
                    pixels[i, j] = palet.dayBeach
                else:
                    pixels[i, j] = palet.nightBeach
            elif noiseValue < 0.3:
                if day == 1:
                    pixels[i, j] = palet.dayLand
                    if trees == 1:
                        checkbox_settings.addTrees(img, size, i, j, treeCounter)
                        treeCounter += 1
                else:
                    pixels[i, j] = palet.nightLand
            elif noiseValue < 0.5:
                if day == 1:
                    pixels[i, j] = palet.dayMountain
                else:
                    pixels[i, j] = palet.nightMountain
            else:
                if day == 1:
                    pixels[i, j] = palet.daySnow
                else:
                    pixels[i, j] = palet.nightSnow

    # Add paths and mask after the base image is created
    if paths == 1:
        checkbox_settings.addPaths(img, size, size/2, size/2, pathCounter)
        pathCounter += 1
    if mask == 1:
        img = checkbox_settings.globeMask(img, size)


    #View the Image
    img.save("new_map.png", "PNG")
    img.show()
