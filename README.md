# FantasyMapGenerator
A desktop application for generating fantasy maps for table top role playing games.

- Version 0.1:
    - Simplex Noise Generation
    - 4 levels of Randomness
        - Number of octaves
        - Amplitude of shape (persistence)
        - Frequency of detail (lacunarity)
        - Seed value from random.random()
    - Day / Night Color Palets

- Version 0.2:
    - Added Mountains / Snow Regions to Generation
    - Refactored range for color placement
    - Updated some comments for better descriptions
    - Switched to file input for generation settings
        - asks for input file from user
        - file format is json

- Version 0.2.1
    - Only update here is the development enviroment being setup

- Version 0.2.2
    - First attempt to have c# call the python script
        - Need to switch from IronPython Library(Does not work with Python3)
    - Static Image used as a placeholder for where the generated maps will go
    - Placeholder "Generate" button (Non functional at the moment)

- To-Do List:
    - Add More Buttons / Sliders / Checkboxes in the Window
    - Add seed value based input
    - Address Resizing of Window
    - Option to mask the map from a shape
    - More detail generation
        - Wavey water
        - Tree Placemnet

