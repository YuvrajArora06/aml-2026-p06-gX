# P06 — Clothing-Item Recognition with Classical Machine Learning

**Course:** Applied Machine Learning (CSAI2017P)  
**Semester:** Autumn 2026  
**Theme:** P06 — Clothing-item recognition with classical machine learning  
**Group:** [Group Number]

## Project Overview

This project investigates how effectively classical machine-learning methods can
classify 28×28 grayscale clothing images from the Fashion-MNIST dataset.

The project compares K-Nearest Neighbours (KNN), Support Vector Machines (SVM),
Random Forests, and a small Multi-Layer Perceptron (MLP) under a common
experimental setup.

Principal Component Analysis (PCA) will be used for dimensionality reduction.
In addition to classification performance, the project will compare model
training and prediction times and investigate which clothing classes are most
frequently confused.

## Research Question

> How far can non-deep methods — PCA with KNN, SVM, random forests, and a small
> MLP — get on 28×28 clothing images, and which classes get confused with which?

## Dataset

The project uses the **Fashion-MNIST** dataset published by Zalando Research.

Dataset source:  
https://github.com/zalandoresearch/fashion-mnist

Fashion-MNIST contains 70,000 grayscale 28×28 images across 10 balanced classes.

The official split will be preserved:

- 60,000 training images
- 10,000 test images

### Classes

| Label | Class |
|---:|---|
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

The raw Fashion-MNIST IDX files will be downloaded manually and stored in
`data/raw/`. A custom IDX loader will be implemented as part of the project.

## Planned Models

- K-Nearest Neighbours (KNN)
- Support Vector Machine (RBF kernel)
- Random Forest
- Multi-Layer Perceptron (MLP)

All models will be compared using the same PCA representation and experimental
protocol.

## Evaluation

The models will be evaluated using:

- Accuracy
- Macro F1-score
- Fit time
- Prediction time
- Per-class precision and recall
- Confusion matrix

The project will also investigate the relationship between the number of PCA
components and classification accuracy.

## Team Members

| Name | Enrolment Number | GitHub Username |
|---|---|---|
| Yuvraj Arora | [Enrolment Number] | YuvrajArora06 |
| [Member 2] | [Enrolment Number] | [GitHub Username] |
| [Member 3] | [Enrolment Number] | [GitHub Username] |
| [Member 4] | [Enrolment Number] | [GitHub Username] |
| [Member 5] | [Enrolment Number] | [GitHub Username] |

## Current Status

**Phase A — Project setup**

The repository and initial project documentation are currently being established.

## Project Workflow

The project is organized into the following experimental stages:

1. Load the official Fashion-MNIST training and test sets using a custom IDX
   loader.
2. Perform exploratory data analysis, including sample visualizations, class
   distributions, mean class images, and pixel-intensity analysis.
3. Scale the image features and fit PCA using training data only.
4. Select the number of principal components using a stated explained-variance
   criterion.
5. Create a validation split from the official training set for model and
   hyperparameter selection.
6. Train and tune KNN, RBF SVM, Random Forest, and MLP classifiers using the
   same PCA representation.
7. Evaluate the selected models on the official Fashion-MNIST test set.
8. Compare accuracy, macro F1-score, fit time, and prediction time.
9. Analyse per-class precision and recall, the confusion matrix, and
   misclassified examples.
10. Perform a PCA component sweep to study the relationship between
    dimensionality and classification performance.

The official 10,000-image test set will not be used for hyperparameter
selection. PCA will be fitted using training data only to avoid data leakage.

## Development Workflow

Project development follows a branch-based Git workflow:

1. Synchronize the local `main` branch with the remote repository.
2. Create a separate branch for each feature, experiment, or documentation task.
3. Commit logically related changes with descriptive commit messages.
4. Push the branch to GitHub.
5. Open a pull request into `main`.
6. Have another team member review the changes before merging.

This workflow keeps individual contributions traceable and allows changes to be
reviewed before they become part of the main project.

## Acknowledgements and Tools

External documentation, tutorials, AI-assisted tools, and other resources used
during the project will be acknowledged here as development progresses.