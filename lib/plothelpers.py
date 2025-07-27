import numpy as np
import matplotlib.pyplot as plt

def plot_comparison(images, titles, cmap="inferno", color_bar=False):
    """
    Plots multiple images side by side for comparison.

    Parameters:
    - images (list of numpy.ndarray): List of images to display.
    - titles (list of str): List of titles corresponding to each image.
    - cmap (str): Color map to use for displaying images (default: "inferno").
    """
    assert len(images) == len(titles), "Number of images and titles must match for correct labeling."

    fig, ax = plt.subplots(1, len(images), figsize=(6 * len(images), 6))

    if len(images) == 1:
        ax = [ax]  # Ensure ax is iterable for a single image

    for i, (image, title) in enumerate(zip(images, titles)):
        ax[i].imshow(image, cmap=cmap, interpolation='none')
        ax[i].set_title(title)
        ax[i].axis("off")  # Hide axes for better visualization
        if(color_bar):
            plt.colorbar(ax[i].imshow(image, cmap=cmap, interpolation='none'), ax=ax[i], orientation='vertical')

    plt.show()

def plot_histogram(ct_data, name, tick_interval=None, log_scale=True):
    """
    Plots a histogram of the flattened CT data.

    Parameters:
    - ct_data: 3D numpy array representing the CT data.
    - name: String to be used in the histogram title.
    - tick_interval: The interval between x-axis ticks (optional).
    - log_scale: Boolean to set y-axis to logarithmic scale (default is True).
    """
    # Flatten the 3D data into a 1D array
    flat_ct_data = ct_data.flatten()

    # Plot the histogram
    plt.figure(figsize=(15, 3))
    plt.hist(flat_ct_data, bins=100)
    plt.title(f'Histogram of {name}')
    plt.xlabel(name)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Set y-axis to logarithmic scale if specified
    if log_scale:
        plt.yscale('log')

    # Set x ticks based on tick_interval if specified
    if tick_interval is not None:
        start_tick = np.floor(flat_ct_data.min() / tick_interval) * tick_interval
        end_tick = np.ceil(flat_ct_data.max() / tick_interval) * tick_interval
        ticks = np.arange(start_tick, end_tick + tick_interval, tick_interval)
        plt.xticks(ticks=ticks)
    
    plt.show()

def plot_image(image: np.ndarray, title: str = "Image", cmap: str = 'inferno'):
    """
    Displays a 2D image using matplotlib with a title and dimensions overlay.

    Parameters:
    - image (np.ndarray): 2D image data to display.
    - title (str): Title of the image (default: "Image").
    - cmap (str): Colormap to use (default: 'inferno').
    """
    if image.ndim != 2:
        raise ValueError("Input must be a 2D array.")

    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap=cmap, interpolation='none')
    plt.title(title)
    plt.colorbar(label='Intensity')
    plt.axis('off')

    # Add dimensions in the lower-left corner
    height, width = image.shape
    plt.text(
        0.01, 0.01, f"{width}×{height}", 
        color='white', fontsize=10, ha='left', va='bottom',
        transform=plt.gca().transAxes, alpha=0.6
    )

    plt.show()