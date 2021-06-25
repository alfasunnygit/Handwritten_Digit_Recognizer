import PIL
from PIL import Image, ImageDraw, ImageOps
from tkinter import *
from keras.models import load_model
import numpy as np
import os
import matplotlib.pyplot as plt

model = load_model('mnist.h5')

width = 500
height = 500
center = height//2
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 128, 0)
r = 25


def save():
    if os.path.exists("image.jpg"):
        os.remove("image.jpg")
    else:
        pass

    filename = "image.jpg"
    image1.save(filename)


def paint(event):
    x1, y1 = (event.x - r), (event.y - r)
    x2, y2 = (event.x + r), (event.y + r)
    cv.create_arc(x1, y1, x2, y2, fill="black", width=8)
    draw.line([x1, y1, x2, y2], fill="black", width=15)


def predict_digit(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img / 255
    res = model.predict([img])[0]
    return np.argmax(res), max(res)


def classify_image():
    im = PIL.Image.open('image.jpg')
    im = ImageOps.invert(im)
    digit, acc = predict_digit(im)
    print("Predicted Digit is:", digit)
    exit(0)


root = Tk()

cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

button = Button(text="save", command=save)
button.pack()

button1 = Button(text="classify", command=classify_image)
button1.pack()

root.mainloop()
