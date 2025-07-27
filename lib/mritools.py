import os
import pydicom
import pandas as pd

def load_dicom_metadata(dicom_folder):
    """
    Load metadata from all DICOM files in a folder.

    Parameters:
        dicom_folder (str): Path to the folder containing DICOM files.

    Returns:
        pandas.DataFrame: DataFrame containing metadata for each DICOM file,
                          including filename, number of slices, shape,
                          modality, and study date.
    """
    metadata = []
    for filename in sorted(os.listdir(dicom_folder)):
        filepath = os.path.join(dicom_folder, filename)
        ds = pydicom.dcmread(filepath)
        
        if "PixelData" in ds:
            shape = ds.pixel_array.shape
            metadata.append({
                'filename': filename,
                'num_slices': shape[0],
                'shape': shape,
                'modality': ds.Modality if 'Modality' in ds else 'Unknown',
                'study_date': ds.StudyDate if 'StudyDate' in ds else 'Unknown'
            })
    
    return pd.DataFrame(metadata)

def load_dicom_data(dicom_folder, file_name):
    """
    Load pixel data from a specific DICOM file.

    Parameters:
        dicom_folder (str): Path to the folder containing DICOM files.
        file_name (str): Filename of the DICOM file to load.

    Returns:
        numpy.ndarray: Pixel data as a NumPy array.

    Raises:
        ValueError: If the file does not contain pixel data.
    """
    file_path = os.path.join(dicom_folder, file_name)
    ds = pydicom.dcmread(file_path)
    
    if "PixelData" in ds:
        return ds.pixel_array
    else:
        raise ValueError(f"File {file_name} does not contain pixel data.")
