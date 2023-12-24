# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:49:48 2023

@author: BISWAJIT
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import random

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Create a lemmatizer object and set of stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Load intents from JSON file
with open("intents_by_me.json", 'r') as file:
    intents = json.load(file)

# Preprocess data
words = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize and lemmatize each word
        w = [lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(pattern) if word.isalnum() and word.lower() not in stop_words]
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = [1 if w in doc[0] else 0 for w in words]
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Shuffle and split data
random.shuffle(training)
train_set, test_set = train_test_split(training, test_size=0.2, random_state=42)

# Convert to NumPy array
train_x = np.array([item[0] for item in train_set])
train_y = np.array([item[1] for item in train_set])
test_x = np.array([item[0] for item in test_set])
test_y = np.array([item[1] for item in test_set])

# Build the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
hist = model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=200, batch_size=5, verbose=1)

# Save the model
model.save("chatbot_model.h5")
print("Model created and saved.")
