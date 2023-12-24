# Sign Language Recognition Project


# Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Project Details](#project-details)
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

## Project Details

**The code part is divided into into three parts:**
1. For Caputring the training and testing data.
2. Train the model & save it.
3. Real-time prediction using the trained model.

### 1. For Caputring the training and testing data.

Here's a breakdown of the main components:

1. **Imports:**
   - `numpy` (as `np`): Numerical operations library.
   - `cv2`: OpenCV library for computer vision.
   - `keras`: High-level neural networks API running on top of TensorFlow or Theano.

2. **Loading the Model:**
   - `model = keras.models.load_model("sign_language_model.h5")`: Loading a pre-trained Keras model for sign language recognition from the file "sign_language_model.h5."

3. **Background Subtraction:**
   - The script initializes variables for background subtraction, with a weighted accumulation mechanism to gradually update the background.
   - `background`: Stores the accumulated background image.
   - `accumulated_weight`: Weight factor for updating the background.

4. **Region of Interest (ROI) Definition:**
   - `ROI_top`, `ROI_bottom`, `ROI_right`, `ROI_left`: Define the region of interest (rectangle) in the captured video frame where hand gestures will be detected.

5. **Dictionary for Mapping:**
   - `word_dict`: A dictionary mapping class indices to corresponding words.

6. **Functions:**
   - `cal_accum_avg(frame, accumulated_weight)`: Function to calculate the accumulated average for background subtraction.
   - `segment_hand(frame, threshold=25)`: Function to segment the hand in the frame based on the difference between the frame and the background.

7. **Camera Initialization:**
   - `cam = cv2.VideoCapture(0)`: Initializes the webcam (assuming the default camera at index 0).

8. **Main Loop:**
   - Captures frames from the webcam in a loop.
   - Performs operations on each frame:
      - Flips the frame horizontally.
      - Defines the region of interest (ROI) in the frame.
      - Converts the ROI to grayscale and applies Gaussian blur.
      - During the first 70 frames, it fetches and updates the background.
      - Afterward, it detects and segments the hand in the frame.
      - Resizes and preprocesses the segmented hand for input to the pre-trained model.
      - Makes predictions using the pre-trained model and displays the recognized sign on the frame.
      - Displays the video feed with rectangles around the ROI and the recognized sign.
      - The loop exits if the 'q' key is pressed.

9. **Clean-up:**
   - Releases the webcam and closes all OpenCV windows.

### 2. Train the model & save it.

This code is for training a convolutional neural network (CNN) using the Keras library with TensorFlow backend for a sign language detection project. Let's break down the code:

1. **Importing Libraries:**
   - TensorFlow and Keras: Deep learning libraries for building and training neural networks.
   - ImageDataGenerator: For real-time data augmentation during training.
   - OpenCV (cv2): For image processing.
   - Matplotlib: For plotting images.
   - Other necessary modules and functions.

2. **Setting Paths:**
   - `train_path` and `test_path` variables represent the paths to the training and testing datasets, respectively.

3. **Data Loading:**
   - `ImageDataGenerator` is used to load and preprocess images from the specified directories (`train_path` and `test_path`).
   - Images are resized to (64, 64) pixels, converted to categorical labels, and loaded in batches of 10.

4. **Plotting Images:**
   - The function `plotImages` is defined to visualize a batch of images. It converts images to RGB format and plots them.

5. **Model Architecture:**
   - A sequential model is created.
   - Convolutional layers (`Conv2D`) with ReLU activation are used for feature extraction.
   - Max pooling layers (`MaxPool2D`) follow each convolutional layer to reduce spatial dimensions.
   - Flattening is done to convert the 2D feature maps into a 1D vector.
   - Dense layers with ReLU activation are used for classification.
   - The final layer has 10 neurons with softmax activation for 10 classes.

6. **Model Compilation:**
   - The model is compiled using the Adam optimizer, categorical crossentropy loss, and accuracy as the evaluation metric.

7. **Callbacks:**
   - `ReduceLROnPlateau`: Reduces the learning rate when a metric has stopped improving.
   - `EarlyStopping`: Stops training when a monitored metric has stopped improving.

8. **Model Training:**
   - The model is trained for 10 epochs with the training data and validated using the test data.
   - Callbacks are applied during training.

9. **Model Evaluation:**
   - Performance metrics (loss and accuracy) are printed on a small batch of test data.
   - The trained model is saved to a file (`sign_language_model.h5`).

10. **Model Loading and Re-evaluation:**
    - The saved model is loaded and evaluated again on a small batch of test data.

11. **Summary and Visualization:**
    - Model summary is printed, and actual vs. predicted labels are displayed for a small set of test data.

12. **Results Visualization:**
    - Training and validation loss/accuracy are plotted over epochs.

Please note that the code includes commented-out sections that show an alternative optimizer (SGD) and its settings. The final model is saved to a file (`sign_language_model.h5`). The loaded model is then evaluated again on a small batch of test data, and the results are displayed.

### 3. Real-time prediction using the trained model.

This Python code uses the OpenCV and Keras libraries to implement a real-time hand sign recognition system using a pre-trained neural network model. Here's a breakdown of the code:

1. **Import Libraries:**
   - `numpy`: Used for numerical operations.
   - `cv2` (OpenCV): Used for computer vision tasks.
   - `keras`: Used for high-level neural networks API.

2. **Load Pre-trained Model:**
   - The Keras model for hand sign recognition is loaded from the "sign_language_model.h5" file.

3. **Initialize Variables:**
   - `background`: Variable to store the background image.
   - `accumulated_weight`: Weight for accumulating the average background.
   - `ROI_top`, `ROI_bottom`, `ROI_right`, `ROI_left`: Define the region of interest (ROI) for hand detection.

4. **Word Dictionary:**
   - A dictionary (`word_dict`) is defined to map the predicted class indices to corresponding words.

5. **Background Accumulation:**
   - The program continuously captures frames from the webcam.
   - It initializes the background by accumulating the weighted average of the first 70 frames.

6. **Hand Segmentation:**
   - Once the background is acquired, it subtracts the current frame from the background to identify the hand.
   - Thresholding and contour detection are used to segment the hand region.

7. **Neural Network Prediction:**
   - The segmented hand region is preprocessed and resized to match the input shape expected by the neural network.
   - The pre-trained model predicts the class of the hand sign.
   - The predicted class is mapped to a word using the `word_dict`.

8. **Display Results:**
   - The original frame is displayed with bounding rectangles around the hand and the region of interest.
   - Information such as the detected word and a message during background acquisition is overlaid on the frame.

9. **User Interface:**
   - The program runs in a loop until the user presses 'q', and it continuously captures frames and performs hand sign recognition.

10. **Clean-up:**
    - After the user exits the program, it releases the webcam and closes all OpenCV windows.

Note: Ensure that the required libraries and the pre-trained model file ("sign_language_model.h5") are available for the code to execute successfully. The hand sign recognition model should be trained beforehand and saved as the specified file.
   
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

The project was inspired by the need for a simple and accessible hand sign recognition system. The pre-trained model was trained on a dataset of hand signs corresponding to digits starting from 1-10.

## Contribution

Feel free to contribute and enhance the project!

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries or issues, please contact Biswajit Jena at 143ahrvzihsahst@gmail.com.
