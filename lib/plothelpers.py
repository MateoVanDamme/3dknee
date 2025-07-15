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