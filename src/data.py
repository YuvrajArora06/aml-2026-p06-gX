import gzip
import struct

import numpy as np


def load_idx_images(filepath):
    """Load images from a gzip-compressed IDX image file."""

<<<<<<< HEAD
    with gzip.open(filepath, "rb") as file:
        header = file.read(16)

        magic, num_images, rows, cols = struct.unpack(">IIII", header)

        if magic != 2051:
            raise ValueError(
                f"Invalid image IDX magic number: {magic}"
            )

        data = np.frombuffer(file.read(), dtype=np.uint8)

        expected_pixels = num_images * rows * cols

        if data.size != expected_pixels:
            raise ValueError(
                f"Expected {expected_pixels} pixels, found {data.size}"
            )

        images = data.reshape(num_images, rows, cols)
=======
    with open(filepath, "rb") as raw_file:
        with gzip.GzipFile(fileobj=raw_file, mode="rb") as file:
            header = file.read(16)

            magic, num_images, rows, cols = struct.unpack(">IIII", header)

            if magic != 2051:
                raise ValueError(
                    f"Invalid image IDX magic number: {magic}"
                )

            data = np.frombuffer(file.read(), dtype=np.uint8)

            expected_pixels = num_images * rows * cols

            if data.size != expected_pixels:
                raise ValueError(
                    f"Expected {expected_pixels} pixels, found {data.size}"
                )

            images = data.reshape(num_images, rows, cols)
>>>>>>> origin/main

    return images


def load_idx_labels(filepath):
    """Load labels from a gzip-compressed IDX label file."""

<<<<<<< HEAD
    with gzip.open(filepath, "rb") as file:
        header = file.read(8)

        magic, num_labels = struct.unpack(">II", header)

        if magic != 2049:
            raise ValueError(
                f"Invalid label IDX magic number: {magic}"
            )

        labels = np.frombuffer(file.read(), dtype=np.uint8)

        if labels.size != num_labels:
            raise ValueError(
                f"Expected {num_labels} labels, found {labels.size}"
            )
=======
    with open(filepath, "rb") as raw_file:
        with gzip.GzipFile(fileobj=raw_file, mode="rb") as file:
            header = file.read(8)

            magic, num_labels = struct.unpack(">II", header)

            if magic != 2049:
                raise ValueError(
                    f"Invalid label IDX magic number: {magic}"
                )

            labels = np.frombuffer(file.read(), dtype=np.uint8)

            if labels.size != num_labels:
                raise ValueError(
                    f"Expected {num_labels} labels, found {labels.size}"
                )
>>>>>>> origin/main

    return labels