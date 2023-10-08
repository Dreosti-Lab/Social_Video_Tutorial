# Load still image, process it with numpy, and save the result to a PNG file

# Import libraries
import numpy as np
import imageio.v3 as iio

# Set paths
input_path = '_data/arena_still.png'
output_path = '_tmp/output.png'

# Load image from file
image = iio.imread(input_path)
print(image.shape)

# Process image (binary threshold)
binary = image > 127

# Convert to output image format (unsigned 8-bit integer, 0 and 255)
output_image = np.uint8(binary) * 255

# Save the processed image to a file
iio.imwrite(output_path, output_image)

#FIN