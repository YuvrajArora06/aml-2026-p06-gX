import numpy as np
from sklearn.model_selection import train_test_split


def flatten_images(images):
    """Flatten 28x28 images into 784-dimensional feature vectors."""

    if images.ndim != 3:
        raise ValueError(
            f"Expected a 3D image array, received shape {images.shape}"
        )

    return images.reshape(images.shape[0], -1)


def scale_pixels(images):
    """Scale uint8 pixel intensities from [0, 255] to [0, 1]."""

    return images.astype(np.float32) / 255.0


def prepare_features(images):
    """Flatten and scale Fashion-MNIST images."""

    flattened = flatten_images(images)
    scaled = scale_pixels(flattened)

    return scaled


def create_validation_split(
    X,
    y,
    validation_size=0.2,
    random_state=42,
):
    """Create a reproducible stratified validation split."""

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=validation_size,
        random_state=random_state,
        stratify=y,
    )

    return X_train, X_val, y_train, y_val