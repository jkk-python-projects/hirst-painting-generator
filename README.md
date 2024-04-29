# Hirst Painting Generator

This repository contains Python practice code that uses turtle graphics to generate a Damien Hirst-like drawing.

## Usage

To generate a Hirst-like painting, follow these steps:

1. Clone the repository using the following command:
   git clone https://github.com/jkk-python-projects/hirst-painting-generator.git

2. Navigate to the cloned directory:
   cd hirst-painting-generator

3. Run the Python script:
   python main.py
   livecodeserver

The script will prompt you to enter the grid size (number of rows and columns), dot size, and the number of colors to use. Once the inputs are provided, the turtle graphics window will open, and the artwork will start generating.

4. Wait for the script to complete. The turtle graphics window will automatically close once the artwork is generated.

5. The generated artwork will be saved as a PNG image file in the same directory as the script, with the filename "hirst_painting.png".

## Customization

You can customize the artwork by modifying the following parameters in the `main.py` script:

- `GRID_SIZE`: Set the number of rows and columns in the grid.
- `DOT_SIZE`: Set the size of each dot in pixels.
- `NUM_COLORS`: Set the number of colors to be randomly assigned to the dots.
- `COLOR_PALETTE`: Define the color palette by specifying RGB tuples. Feel free to add or remove colors according to your preference.

## Requirements

- Python 3.x
- Turtle graphics library (included in Python standard library)

## Contributing

Contributions to this repository are currently not open. If you encounter any issues or have suggestions, you can submit them through the repository's issue tracker.

## License

The code in this repository is not explicitly licensed, so standard copyright laws apply.
