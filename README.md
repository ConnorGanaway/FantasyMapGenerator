# FantasyMapGenerator
A desktop application for generating fantasy maps for table top role playing games.

![Python package](https://github.com/ConnorGanaway/FantasyMapGenerator/actions/workflows/actions.yml/badge.svg)

- Version 1.0.3
    - Trees will not be added after all inital pixels are colored (Pixel art was being pasted over)

- Version 1.0.2
    - Paths will now be connected instead of random dots

- Version 1.0.1
    - Renamed "noise_gen.py" to "map_gen.py"
    - Moved checkbox functions and color palet to seperate files

- Version 1.0
    - Reorganized Checkboxes on UI
    - All features planned are implemented

- Version 0.9
    - Implemented Globe Mask for the Map

- Version 0.8
    - Improved Path generation

- Version 0.7
    - Redesigned GUI
        - Image will no longer be apart of the app
    - Ability to import / export settings file
    - More temporary generation settings
        - Paths Checkbox
        - Buildings Checkbox
    - When a random seed is used it will display in the textbox
    - Improved map file reference when interfacing with the generation script

- Version 0.6
    - Function to add a single Tree

- Version 0.5
    - Desktop App now interfaces with the Python Script
    - Newly generated map is launching in a seperate window
    - Seed input is now factored into the script
        - Not fully idependent of the computer seed yet (Need to create toggle when user input is gathered)

- Version 0.4:
    - Adjusted the proper ranges for the sliders
    - When generated is clicked it writes the information to a json file
    - If no seed value is given, a random 16 character phrase is generated in its place

- Version 0.3:
    - Basic GUI layout (Subject to change)
        - Size / Seed Input has no functionality yet
        - The 4 sliders are binded to a label to show their current value (These represent the values for the simplex noise function)
        - Checkboxs
            - Dark Mode
            - Generate Paths
            - TBD feature 3 (Currently being used as reset for the sliders)
            - TBD feature 4
    - Clicking the Genrate Button will only show and hide a default image
        - This will be replace with the script later

- Version 0.2.2:
    - First attempt to have c# call the python script
        - Need to switch from IronPython Library(Does not work with Python3)
        - Will return to this later
    - Static Image used as a placeholder for where the generated maps will go
    - Placeholder "Generate" button (Non functional at the moment)

- Version 0.2.1:
    - Only update here is the development enviroment being setup

- Version 0.2:
    - Added Mountains / Snow Regions to Generation
    - Refactored range for color placement
    - Updated some comments for better descriptions
    - Switched to file input for generation settings
        - asks for input file from user
        - file format is json

- Version 0.1:
    - Simplex Noise Generation
    - 4 levels of Randomness
        - Number of octaves
        - Amplitude of shape (persistence)
        - Frequency of detail (lacunarity)
        - Seed value from random.random()
    - Day / Night Color Palets
