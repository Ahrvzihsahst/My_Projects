# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:11:52 2023

@author: BISWAJIT
"""

import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model
from keras.optimizers import SGD

# Load the trained model to classify the images
custom_objects = {'SGD': SGD}  # Add other custom objects if needed
model = load_model(r'D:\My Prog\Naresh_i _Technology\Resume Project\Image Classification Using cifar-10 dataset\model1_cifar_50epoch.h5',custom_objects=custom_objects)

# Dictionary to label all the CIFAR-10 dataset classes.
classes = {
    0: 'aeroplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}

# Initialize GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Image Classification CIFAR10 \n Upload image of size 32*32 pixels')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    global label
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = np.argmax(model.predict(image), axis=-1)[0]
    sign = classes[pred]
    label.configure(foreground='#011638', text=sign)

def show_classify_button(file_path):
    classify_button = Button(top, text="Classify Image",
                             command=lambda: classify(file_path), padx=10, pady=5)
    classify_button.configure(background='#364156', foreground='white',
                               font=('arial', 10, 'bold'))
    classify_button.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25),
                            (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except Exception as e:
        print(e)

upload_button = Button(top, text="Upload an image", command=upload_image,
                       padx=10, pady=5)
upload_button.configure(background='#364156', foreground='white',
                         font=('arial', 10, 'bold'))
upload_button.pack(side=tk.BOTTOM, pady=50)

sign_image.pack(side=tk.BOTTOM, expand=True)
label.pack(side=tk.BOTTOM, expand=True)

heading = Label(top, text="Image Classification CIFAR10", pady=20,
                font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
