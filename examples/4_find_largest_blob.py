# Load still image, compute difference, and find largest binary blob

# Import libraries
import numpy as np
import imageio.v3 as iio
from skimage.measure import label, regionprops, regionprops_table

# Set paths
foreground_path = '_data/arena_still.png'
background_path = '_data/arena_empty.png'
output_path = '_tmp/output.png'

# Load image from file
foreground_image = iio.imread(foreground_path)
background_image = iio.imread(background_path)

# Convert to floating point precision
foreground_image_float = np.float32(foreground_image)
background_image_float = np.float32(background_image)

# Process images (absolute difference, crop, and threshold)
difference = np.abs(foreground_image_float - background_image_float)
crop_image = difference[:, :175]
binary_image = np.uint8(crop_image > 10)

# Find binary regions
label_image = label(binary_image)
blobs = regionprops(label_image)
num_blobs = len(blobs)

# Find largest binary region
largest_area = 0
largest_id = -1
id = 0
for blob in blobs:
    if blob.area > largest_area:
        largest_id = 0
largest_blob = blobs[largest_id]

# Report
print("Blob Area: {0:.1f}, Blob Centroid: {1:.2f},{2:.2f}".format(largest_blob.area, largest_blob.centroid[0], largest_blob.centroid[1]))

# Convert to output image format (unsigned 8-bit integer, 0 and 255)
output_image = np.uint8(binary_image * 255)

# Save the processed image to a file
iio.imwrite(output_path, output_image)

#FIN