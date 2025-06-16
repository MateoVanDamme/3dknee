import numpy as np
import nrrd
from scipy.ndimage import gaussian_filter

def filter_and_subsample(ct_data, subsampling_factor=2, sigma=1):
    """
    Applies a Gaussian filter to the CT data and then subsamples it.

    Parameters:
    - ct_data (np.ndarray): The original CT data (3D numpy array).
    - subsampling_factor (int): The factor by which to downsample the data (default: 2).
    - sigma (float): Standard deviation for Gaussian kernel (default: 1).

    Returns:
    - np.ndarray: The filtered and downsampled data.
    """
    if subsampling_factor == 1:
        return ct_data

    filtered_data = gaussian_filter(ct_data, sigma=sigma)
    ct_data_scaled = filtered_data[::subsampling_factor, ::subsampling_factor, ::subsampling_factor]
    return ct_data_scaled

def save_ct_nrrd(filename, ct_data):
    """
    Saves CT data as a compressed NRRD file with basic metadata.

    Parameters:
    - filename (str): The output NRRD file path.
    - ct_data (np.ndarray): 3D NumPy array of CT data.
    """
    center_of_mass = np.array([0, 0, 0])  # Placeholder; could be calculated later

    header = {
        'type': 'float',
        'dimension': 3,
        'space': 'left-posterior-superior',
        'sizes': ct_data.shape[::-1],  # (z, y, x)
        'encoding': 'gzip',
        'endian': 'little',
        'space directions': np.eye(3).tolist(),
        'center of rotation': center_of_mass.tolist()
    }

    nrrd.write(filename, ct_data, header)
    print(f"Saved as {filename}")
