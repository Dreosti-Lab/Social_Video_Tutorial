# Load video, compute median pixel values

# Import libraries
import imageio.v3 as iio
import numpy as np

# Set paths
input_path = '_data/arena_video.avi'
output_path = '_data/output.png'

# Load video (and metadata)
video_metadata = iio.immeta(input_path, exclude_applied=False)
video_frames = iio.imread(input_path, index=None)
print(video_frames.shape)

# Extract red frames
red_frames = video_frames[:,:,:,0]

# Compute median value for each pixel
median = np.median(red_frames, 0)

# Convert to output image format (unsigned 8-bit integer)
output_image = np.uint8(median)

# Save the processed image to a file
iio.imwrite(output_path, output_image)

#FIN