from PIL import Image, ImageFilter
import noise
import numpy as np
import random
import sys

# Map Color Palets for Day / Night Versions
dayWater = (65,105,225)
nightWater = (0, 0, 51)

dayBeach = (238, 214, 175)
nightBeach = (51, 25, 0)

dayLand = (34,139,34)
nightLand = (0, 51, 0)


if __name__ == "__main__":

    # Map Size (square; pixel X pixel), and the color palet to choose (day = 1, night = 0)
    size = 500
    day = 1

     # The level of zoom for the map
    scale = 100.0            
    
    # How to change the "sharpness" of the lines
    octaves = 6               
    persistence = 0.5         
    lacunarity = 2.0 

    # The noise function (snoise2) does not randomize without this value!
    seed = random.random() 

    #Terminal Debug Print Statements
    print("Map: ", size)
    if day == 1:
        print("Day Time")
    else:
        print("Night Time")


    #Create a new blank image and save the pixels
    img  = Image.new( mode = "RGB", size = (int(size), int(size)), color = (0, 0, 0) )
    pixels = img.load()

    # Using the snoise2 function and sliders above, generate the pixel height map values
    for i in range(int(size)):
        for j in range(int(size)):
            value = noise.snoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=size, repeaty=size, base=seed)

            # Based on the value generate, color the pixel accordingly
            if value < -0.05:
                if day == 1:
                    pixels[i, j] = dayWater
                else:
                    pixels[i, j] = nightWater
            elif value < 0:
                if day == 1:
                    pixels[i, j] = dayBeach
                else:
                    pixels[i, j] = nightBeach
            elif value < 1.0:
                if day == 1:
                    pixels[i, j] = dayLand
                else:
                    pixels[i, j] = nightLand

    #View the Image     
    img.show()