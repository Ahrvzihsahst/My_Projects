# Sign Language Recognition Project


# Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Acknowledgments](#acknowledgments)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)


## Overview
This project is a real-time sign language recognition system implemented in Python, utilizing computer vision techniques and deep learning. The system leverages OpenCV for image processing and Keras for deep learning. The goal is to identify hand signs captured by a webcam and map them to corresponding words using a pre-trained neural network model. The system serves as a simple yet effective solution for recognizing and interpreting hand signs in real-time scenarios.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Keras (`pip install keras`)
- TensorFlow (or Theano)

## Project Structure

- `sign_language_model.h5`: Pre-trained Keras model for hand sign recognition.
- `sign_language_recognition.py`: Python script implementing the hand sign recognition system.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sign-language-recognition.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sign-language-recognition
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
Download the pre-trained model (`sign_language_model.h5`) and place it in the project directory.
4. Run the `sign_language_recognition.py` script:

   ```bash
   python sign_language_recognition.py
   ```

   1. The script will open a webcam feed, and you can use hand signs in front of the camera to see real-time recognition results.
   2. Allow the webcam access.
   3. The system will start capturing video frames, and the recognized sign will be displayed in the video feed window.
   4. Press 'q' to exit the application.

## Features
- **Real-time Hand Sign Recognition:** The system captures video frames from a webcam in real-time and recognizes hand signs within a specified region of interest (ROI).
- **Background Subtraction:** The background subtraction technique is employed to isolate the hand from the background, enhancing the accuracy of sign detection.
- **Pre-trained Model:** The project uses a pre-trained Keras model (`sign_language_model.h5`) for sign language recognition. The model is loaded and applied to predict the sign based on the segmented hand.
- **Region of Interest (ROI):** The region of interest (ROI) is defined in the captured video frame, focusing on the area where hand gestures will be detected.
- **Model Loading and Prediction:** The pre-trained Keras model (`sign_language_model.h5`) is loaded to recognize hand signs. The recognized signs are displayed on the video feed in real-time.
- **User Interface:** The video feed is displayed in a window with rectangles drawn around the ROI and the recognized sign, providing a user-friendly interface.
- **User Interaction** Press 'q' to exit the application.

## Configuration
- Adjust the ROI parameters (`ROI_top`, `ROI_bottom`, `ROI_right`, `ROI_left`) in the script to fine-tune the region where hand signs are detected.
- Modify the `word_dict` dictionary to customize the mapping of class indices to words.


## Acknowledgments

The project was inspired by the need for a simple and accessible hand sign recognition system. The pre-trained model was trained on a dataset of hand signs corresponding to different words.

## Contribution

Feel free to contribute and enhance the project!

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries or issues, please contact Biswajit Jena at 143ahrvzihsahst@gmail.com.
