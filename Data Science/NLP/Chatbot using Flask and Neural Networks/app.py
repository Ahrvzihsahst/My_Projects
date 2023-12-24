# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:19:09 2023

@author: BISWAJIT
"""

from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import json
import random

app = Flask(__name__)

# Load the trained chatbot model
model = load_model("chatbot_model.h5")

# Load NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Load intents from JSON file
with open("intents_by_me.json", 'r') as file:
    intents = json.load(file)

# Preprocess data
words = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = [lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(pattern) if word.isalnum()]
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

def clean_up_sentence(sentence):
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(sentence) if word.isalnum()]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

@app.route('/')
def index():
    return render_template('test_index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the frontend
        user_input = request.json['message']

        # Predict intent using the trained model
        p = bow(user_input, words, show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        # Get the most probable intent
        results.sort(key=lambda x: x[1], reverse=True)
        intent = classes[results[0][0]]

        # Find the appropriate response
        for i in intents['intents']:
            if i['tag'] == intent:
                response = random.choice(i['responses'])
                break

        # Return the response to the frontend
        return jsonify({'message': response})

    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal Server Error'})

if __name__ == '__main__':
    app.run(debug=True)
