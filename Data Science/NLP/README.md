# Chatbot Implementation using Flask and Neural Networks
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
This project combines natural language processing (NLP) techniques and neural networks to implement a chatbot capable of recognizing user input patterns and classifying them into predefined intents. The chatbot employs a bag-of-words representation and utilizes a neural network for both training and prediction.The accompanying repository features Python scripts designed to deploy the chatbot within a web browser, leveraging the Flask web framework. The chatbot is fueled by a neural network model trained on NLP techniques, providing an interactive and responsive conversational experience.
## Requirements
- Python
- Flask
- TensorFlow
- Keras
- NLTK
- HTML
- CSS
- JavaScript

Install the required packages using:
```bash
pip install flask tensorflow nltk
```

## Project Structure
- `chatbot_model.h5`: Pre-trained chatbot model.
- `intents_by_me.json`: JSON file containing predefined intents for the chatbot.
- `app.py`: Flask application for deploying the chatbot in a browser.
- `templates/index.html`: HTML template for the chatbot interface.

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Access the chatbot interface in your browser (typically at http://127.0.0.1:5000/).
3. Interact with the chatbot by entering messages and receiving responses.
   
## Project Details
The project involves two main components: the training of a chatbot model and the deployment of the chatbot using a Flask web application.

### Chatbot Model Training:

Here's a breakdown of the main components and steps involved:

1. **Imports:**
   - `nltk`: Natural Language Toolkit library for NLP.
   - `stopwords`: Set of common English words to be ignored.
   - `WordNetLemmatizer`: Tool for lemmatizing words.
   - `json`: For handling JSON data.
   - `numpy`: Library for numerical operations.
   - `train_test_split`: From scikit-learn for splitting data.
   - `Sequential`, `Dense`, `Dropout`: Keras components for building neural networks.
   - `SGD`: Stochastic Gradient Descent optimizer.

2. **Download NLTK Resources:**
   - Downloads necessary resources for tokenization and lemmatization.

3. **Load Intents from JSON:**
   - Reads intents from a JSON file (`intents_by_me.json`).

4. **Preprocess Data:**
   - Tokenizes, lemmatizes, and preprocesses text data.
   - Constructs a vocabulary (`words`) and a list of classes (`classes`).
   - Prepares training data in the format expected by a neural network.

5. **Create Training Data:**
   - Converts patterns into a bag of words representation.
   - Creates training data with input (bag of words) and output (intent label).

6. **Shuffle and Split Data:**
   - Shuffles and splits the training data into training and testing sets.

7. **Build the Model:**
   - Defines a simple neural network using Keras Sequential model.
   - Three layers: input, hidden (with dropout), and output.
   - Uses softmax activation for multiclass classification.

8. **Compile the Model:**
   - Configures the model with categorical cross-entropy loss and Stochastic Gradient Descent (SGD) optimizer.

9. **Train the Model:**
   - Fits the model to the training data, validating on the test set.
   - Training for 200 epochs with a batch size of 5.

10. **Save the Model:**
    - Saves the trained model to a file (`chatbot_model.h5`).
   
### Chatbot Deployment using Flask:

1. **Flask Web Framework Setup:**
   - Imports the necessary modules from Flask.
   - Defines a Flask web application instance named `app`.

2. **Chatbot Model Loading:**
   - Loads a pre-trained chatbot model from a file named "chatbot_model.h5" using TensorFlow's Keras module.

3. **Natural Language Toolkit (NLTK) Setup:**
   - Downloads NLTK resources for tokenization and lemmatization.
   - Initializes a WordNet lemmatizer.

4. **Intents Loading:**
   - Loads intents for the chatbot from a JSON file named "intents_by_me.json."

5. **Data Preprocessing:**
   - Extracts words, classes, and documents from the loaded intents.
   - Performs lemmatization and tokenization on patterns in the intents.

6. **Functions for Sentence Cleanup and Bag of Words (BoW) Conversion:**
   - `clean_up_sentence`: Tokenizes and lemmatizes a given sentence.
   - `bow`: Converts a sentence into a bag-of-words representation based on the loaded words.

7. **Flask Routes:**
   - `/`: Renders the main HTML template named "index.html" when accessing the root URL.
   - `/api/chat` (POST method): Handles chat interactions. Accepts user input, predicts intent using the trained model, selects a response based on the intent, and returns the response in JSON format.

8. **Main Function:**
   - Checks if the script is being run directly (`__name__ == '__main__'`) and starts the Flask application in debug mode.

## Configuration
- Adjust the model training parameters, such as epochs and batch size, in the `app.py` script.
- Modify the JSON file (`intents_by_me.json`) to customize the predefined intents and responses.

## Acknowledgments
- This project uses Flask for web application development and TensorFlow with Keras for neural network modeling.
- Natural Language Toolkit (NLTK) is employed for text processing tasks.

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries, please contact the project owner:
- Name: Biswajit
- Email: [143ahrvzihsahst@email.com](mailto:example@email.com)
