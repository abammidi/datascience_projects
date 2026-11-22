# MNIST Digit Classifier (PyTorch CNN)

Status: Completed (DSC 550 assignment). The notebook's saved outputs are from the original run. See the evaluation note for the caveat on the test set.

## Overview

This project trains a convolutional neural network to classify handwritten digits (0–9) from the MNIST dataset, using PyTorch. It loads the data, shows sample images with their labels, trains the model for three epochs, reports test accuracy, and shows a confusion matrix.

## Model

Two convolution layers (32 and 64 filters, 3×3, with ReLU and 2×2 max pooling), dropout of 0.25, and two fully connected layers (128 and 10 outputs). Adam optimizer, learning rate 0.001, batch size 128, cross-entropy loss.

## Results

- Training accuracy after epoch 3: 98.7%.
- Test accuracy after epoch 3: 98.89% (10,000 test images).

## Contents

- `mnist_cnn_classifier.ipynb`: the notebook, with outputs from the original run.

## Requirements and data

Requires `torch`, `torchvision`, `scikit-learn`, and `matplotlib`. The notebook downloads MNIST to `./data` on first run. If downloads are blocked, download MNIST once on a machine with internet access and place it in `./data`.

## Evaluation note

Test accuracy was printed after every epoch for monitoring. The notebook does not have a separate validation split, so the test set was seen during training. The 98.89% figure is the accuracy after three epochs. If the epoch count was chosen by looking at test scores, the figure overstates performance on unseen data. A validation split would give an unbiased estimate; that is the recommended next step.

## Known limitations

- No validation split (see above).
- The model was trained for three epochs. Longer training or a learning-rate schedule may improve accuracy; the notebook's summary lists these as options.
- Edits since the original run changed only a code comment and a markdown cell. The code and the saved outputs are unchanged, but the notebook was not re-run in this environment, which lacks PyTorch.
