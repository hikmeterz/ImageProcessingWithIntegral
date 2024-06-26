﻿# ImageProcessingWithIntegral

## Project Description
This repository contains Python scripts that perform image processing tasks using integral images. The provided scripts implement two main functionalities: computing integral images and applying box filters using integral images. The repository includes detailed implementations of these techniques and provides example usage on sample images.

## Files
- `IntegralProcess.py`: Python script implementing the image processing tasks.
- `lena_grayscale_hq.jpg`: Sample grayscale image used for testing the scripts.
- `rapor.pdf`: Project report describing the implementation and results of the image processing tasks.

## Python Script Descriptions

### `IntegralProcess.py`
This Python script contains two main functions: `question_1()` and `question_2()`. Both functions perform image processing tasks using integral images.

#### Key Features:
- **`question_1()`**: Computes the integral image of a given grayscale image and compares it with OpenCV's implementation.
- **`question_2()`**: Applies a box filter to the integral image using a 3x3 filter window.

#### Example Workflow

1. **Computing Integral Image (question_1)**
   - The function reads a grayscale image, computes its integral image, and compares it with OpenCV's integral image function.
   - Displays the difference between the computed integral image and OpenCV's result.

2. **Applying Box Filter (question_2)**
   - The function reads a grayscale image and computes its integral image.
   - Applies a 3x3 box filter to the integral image.
   - Displays the filtered image.

### Example Usage
To run the script and perform the image processing tasks, execute the following commands:
