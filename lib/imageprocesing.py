import numpy as np
from scipy.ndimage import gaussian_filter
import cv2

def filter_and_subsample(data, subsampling_factor=2, sigma=1):
    """
    Applies a Gaussian filter to 3D data and then subsamples it.

    Parameters:
    - data (np.ndarray): The original 3D data array.
    - subsampling_factor (int): The factor by which to downsample the data (default: 2).
    - sigma (float): Standard deviation for the Gaussian kernel (default: 1).

    Returns:
    - np.ndarray: The filtered and downsampled data.
    """
    original_shape = data.shape

    if subsampling_factor == 1:
        print(f"Volume size unchanged: {original_shape}")
        return data

    filtered_data = gaussian_filter(data, sigma=sigma)
    downsampled_data = filtered_data[::subsampling_factor, ::subsampling_factor, ::subsampling_factor]
    print(f"Volume size before: {original_shape}, after: {downsampled_data.shape}")
    return downsampled_data

def clip_and_normalize(ct_data, min_val, max_val):
    """
    Clips and normalizes the CT data.

    Parameters:
    - ct_data: 3D numpy array representing the CT data.
    - min_val: Minimum value for clipping.
    - max_val: Maximum value for clipping.

    Returns:
    - ct_data_normalized: The normalized CT data.
    """
    # Clip HU values to the specified range
    ct_data_clipped = np.clip(ct_data, min_val, max_val)

    # Normalize the clipped data to the range [0, 1]
    ct_data_normalized = (ct_data_clipped - min_val) / (max_val - min_val)

    # Cast to float32 (Three.js expects float data)
    ct_data_normalized = ct_data_normalized.astype(np.float32)

    return ct_data_normalized

def remove_fabric_artifacts(data, erosion_kernel_size, dilation_kernel_size, threshold=0.1):
    """
    Applies erosion followed by dilation to remove fabric artifacts from a CT scan.

    Parameters:
    - data (numpy.ndarray): 3D CT scan volume.
    - erosion_kernel_size (int): Size of the erosion kernel.
    - dilation_kernel_size (int): Size of the dilation kernel.
    - threshold (float): Threshold for binary mask.

    Returns:
    - cleaned_data (numpy.ndarray): CT scan with fabric artifacts removed.
    """
    
    cleaned_data = np.copy(data)  # Copy to avoid modifying original

    # Define kernels
    erosion_kernel = np.ones((erosion_kernel_size, erosion_kernel_size), np.uint8)
    dilation_kernel = np.ones((dilation_kernel_size, dilation_kernel_size), np.uint8)

    # Iterate over each slice
    for i in range(data.shape[0]):
        slice_data = data[i]

        # Create a binary mask
        binary_mask = (slice_data > threshold).astype(np.uint8)

        # Apply erosion
        eroded_mask = cv2.erode(binary_mask, erosion_kernel, iterations=1)

        # Apply dilation
        dilated_mask = cv2.dilate(eroded_mask, dilation_kernel, iterations=1)

        # Apply mask to remove fabric
        cleaned_data[i] = slice_data * dilated_mask  # Zero out unwanted areas

    return cleaned_data