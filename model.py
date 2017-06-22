import csv
import time
import cv2
import numpy as np
import tensorflow as tf
tf.python.control_flow_ops = tf

# Read in .csv file containing references to training imagery and steering data
lines = []
with open('newlog.csv') as csvfile:
    reader = csv.reader(csvfile)
    numLines = 0
    for line in reader:
        if numLines == 0:
            numLines += 1 # Don't process first line with header text in fields
        else:
            numLines += 1
            lines.append(line)

localtime = time.asctime(time.localtime(time.time()))
print(localtime, "Number of lines read from .csv input file:", str(len(lines)))

# Read in the image file paths, along with associated steering measurements
# from each line in input training data file, and store them in images
# and measurements lists.
images = []
measurements = []
#evenLine = True
#numLines = 0
for line in lines:
    path = line[0]
    image = cv2.imread(path)
    measurement = float(line[3])
# Code below, to flip every other image, is commented out, as it did not help performance
# of the model during test runs.
# Flip every other image, so as to reduce "left turn bias"
#    numLines += 1
#    if evenLine:
#        evenLine = False
#    else:
#        evenLine = True
#        image = np.fliplr(image)
#        measurement = -measurement
    images.append(image)
    measurements.append(measurement)

# Put the training data into X_train and y_train numpy arrays,
# as required by Keras(and underlying TensorFlow) model.fit() method.
y_train = np.array(measurements)
X_train = np.array(images)
localtime = time.asctime(time.localtime(time.time()))
print (localtime, "X_train & y_train np.array structures created, defining Keras NN model")

# Keras library module imports
from keras.models import Sequential
from keras.layers import Lambda
from keras.layers.core import Dense, Flatten
from keras.layers.convolutional import Convolution2D, Cropping2D

# Implement Keras Neural Network, based on NVIDIA CNN architecture
# described in the paper: arXiv.1604.073116v1 [cs.CV] 25 Apr 2016
# - Lambda layer provides image normalization.
# - Python generator not used, as training this model with 5 Epochs produces
#   great results at only ~58 seconds per epoch on a GTX1060 graphics card;
#   so the extra complexity is not warrented.
# - Over-fitting is avoided by keeping training passes to about 5 Epochs,
#   when using less than 10,000 training data samples.
# - Adam Optimizer used to auto-tune learning rate parameters during training.
model = Sequential()
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Convolution2D(24, 5, 5, subsample=[2,2], activation='relu'))
model.add(Convolution2D(36, 5, 5, subsample=[2,2], activation='relu'))
model.add(Convolution2D(48, 5, 5, subsample=[2,2], activation='relu'))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='tanh'))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, nb_epoch=5, validation_split=0.2, shuffle=True)

model.save('model.h5')
