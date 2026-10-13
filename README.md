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

## Acknowledgements and Tools

External documentation, tutorials, AI-assisted tools, and other resources used
during the project will be acknowledged here as development progresses.