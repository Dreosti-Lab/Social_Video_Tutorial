# Load still images (foreground and background), compute difference with numpy, and save the result to a PNG file

# Import libraries
import numpy as np
import imageio.v3 as iio

# Set paths
foreground_path = '_data/arena_still.png'
background_path = '_data/arena_empty.png'
output_path = '_data/output.png'

# Load image from file
foreground_image = iio.imread(foreground_path)
background_image = iio.imread(background_path)

# Convert to floating point precision
foreground_image_float = np.float32(foreground_image)
background_image_float = np.float32(background_image)

# Process images (absolute difference)
difference = np.abs(foreground_image_float - background_image_float)

# Convert to output image format (unsigned 8-bit integer)
output_image = np.uint8(difference)

# Save the processed image to a file
iio.imwrite(output_path, output_image)

#FIN