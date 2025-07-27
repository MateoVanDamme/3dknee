import numpy as np
import nrrd

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


def print_nrrd_header(filename):
    """Reads an NRRD file and prints its header information."""
    data, header = nrrd.read(filename)
    print(f"NRRD Header for {filename}:")
    for key, value in header.items():
        print(f"{key}: {value}")
    print()  # Add a newline for readability