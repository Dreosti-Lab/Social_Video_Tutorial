# Load video, and for each frame: compute difference and find largest binary blob

# Import libraries
import numpy as np
import imageio.v3 as iio
from skimage.measure import label, regionprops, regionprops_table

# Set paths
input_path = '_data/arena_video.avi'
background_path = '_data/arena_empty.png'
output_path = '_tmp/output.png'

# Load background image from file
background_image = iio.imread(background_path)

# Load video (and metadata)
video_metadata = iio.immeta(input_path, exclude_applied=False)
video_frames = iio.imread(input_path, index=None)
num_frames = video_frames.shape[0]

# Convert to floating point precision
background_image_float = np.float32(background_image)
video_frames_float = np.float32(video_frames)

# Find largest blob in all video frames
for i in range(num_frames):
    # Extract current frame
    frame = video_frames[i, :,:,0]

    # Process images (absolute difference, crop, and threshold)
    difference = np.abs(frame - background_image_float)
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
    print("{0}: Blob Area: {1:.1f}, Blob Centroid: {2:.2f},{3:.2f}".format(i, largest_blob.area, largest_blob.centroid[0], largest_blob.centroid[1]))

#FIN