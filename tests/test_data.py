import numpy as np

from src.data import load_idx_images, load_idx_labels


TRAIN_IMAGES_PATH = "data/raw/train-images-idx3-ubyte.gz"
TRAIN_LABELS_PATH = "data/raw/train-labels-idx1-ubyte.gz"

TEST_IMAGES_PATH = "data/raw/t10k-images-idx3-ubyte.gz"
TEST_LABELS_PATH = "data/raw/t10k-labels-idx1-ubyte.gz"


def test_training_shapes():
    images = load_idx_images(TRAIN_IMAGES_PATH)
    labels = load_idx_labels(TRAIN_LABELS_PATH)

    assert images.shape == (60000, 28, 28)
    assert labels.shape == (60000,)


def test_test_shapes():
    images = load_idx_images(TEST_IMAGES_PATH)
    labels = load_idx_labels(TEST_LABELS_PATH)

    assert images.shape == (10000, 28, 28)
    assert labels.shape == (10000,)


def test_training_class_counts():
    labels = load_idx_labels(TRAIN_LABELS_PATH)

    unique_labels, counts = np.unique(labels, return_counts=True)

    assert np.array_equal(unique_labels, np.arange(10))
    assert np.all(counts == 6000)


def test_label_range():
    train_labels = load_idx_labels(TRAIN_LABELS_PATH)
    test_labels = load_idx_labels(TEST_LABELS_PATH)

    assert train_labels.min() == 0
    assert train_labels.max() == 9

    assert test_labels.min() == 0
    assert test_labels.max() == 9


def test_image_dtype_and_range():
    images = load_idx_images(TRAIN_IMAGES_PATH)

    assert images.dtype == np.uint8
    assert images.min() == 0
    assert images.max() == 255