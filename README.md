# CarND-P3-BC-StewartTeaze
Stewart Teaze's GitHub repository for Udacity Self-Driving Car Nanodegree Term1 Project3 - Behavioral Cloning
# Behaviorial Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Overview
---
Stewart Teaze's GitHub repository for Udacity Self-Driving Car Nanodegree Term1 Project3 - Behavioral Cloning

This project trains a convolutional neural network model to clone driving behavior. The model is trained, validated and tested by invoking Keras high-level neural networks API functions. The model will output a steering angle to an autonomous vehicle, operating with a Simulated driving environment.  Image data and steering angles are used to train the model (in the Simulator, operating in "Training Mode"), and this model is then used to drive the car autonomously around the track (in the Simulator, operating in "Autonomous Mode").

To meet project specifications, this project submission includes these five required files: 
* model.py (script used to create and train the model)
* drive.py (script to drive the car)
* model.h5 (trained Keras model)
* writeup_report.pdf
* video.mp4 (a video recording of the vehicle driving autonomously around the track for one full lap)

This project development utilized the following directories of baseline (center) and "recovery" driving image/steering-command
recordings; however, these directories/files are specifically not included in the repository, as they would exceed the size of the
github repository limit, and we were specifically instructed not to include these files in the project submission.
* IMG (baseline/centered driving image/steering-command recordings, of about 8000 sample images/steering-commands)
* run7 ("General" recovery sequence recordings from various off-center situations, about 250 images/commands)
* run12 ("Specific" recovery sequence recording of getting too-close to right edge in treacherous/most-onerous "brown curve")

This project's repository does include the following .csv files; the first three are associated with, and reference the contents of,
the 3 image recording directories discussed above - the last file, newlog.csv, is built by including the contents of all three of the
first .csv files listed below, and is the file referenced in the project's model.py source code:
* driving_log.csv
* run7.csv
* run12.csv
* newlog.csv

The Project
---
The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior 
* Design, train and validate a model that predicts a steering angle from image data
* Use the model to drive the vehicle autonomously around the first track in the simulator. The vehicle should remain on the road for an entire loop around the track.
* Summarize the results with a written report

## The Simulator

The Udacity Driving Simulator can be downloaded from the Behavioral Cloning classroom lesson 2: Project Resources.

Refer to the writeup_report.pdf file, and classroom lesson 3: Running the Simulator, for details on the usage and operation of the Udacity Simulator.

## Details About the Usage of the Udacity-Provided Project Support Python Scripts drive.py and video.py

### `drive.py`

Usage of `drive.py` requires you have saved the trained model as an h5 file, i.e. `model.h5`. See the [Keras documentation](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model) for how to create this file using the following command:
```sh
model.save(filepath)
```

Once the model has been saved, it can be used with drive.py using this command:

```sh
python drive.py model.h5
```

The above command will load the trained model and use the model to make predictions on individual images in real-time and send the predicted angle back to the server via a websocket connection.

#### Saving a video of the autonomous agent

```sh
python drive.py model.h5 run1
```

The fourth argument, `run1`, is the directory in which to save the images seen by the agent. If the directory already exists, it'll be overwritten.

```sh
ls run1

[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_424.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_451.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_477.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_528.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_573.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_618.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_697.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_723.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_749.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_817.jpg
...
```

The image file name is a timestamp of when the image was seen. This information is used by `video.py` to create a chronological video of the agent driving.

### `video.py`

```sh
python video.py run1
```

Creates a video based on images found in the `run1` directory. The name of the video will be the name of the directory followed by `'.mp4'`, so, in this case the video will be `run1.mp4`.

Optionally, one can specify the FPS (frames per second) of the video:

```sh
python video.py run1 --fps 48
```

Will run the video at 48 FPS. The default FPS is 60.

#### Why create a video

1. It's been noted the simulator might perform differently based on the hardware. So if your model drives succesfully on your machine it might not on another machine (your reviewer). Saving a video is a solid backup in case this happens.
2. You could slightly alter the code in `drive.py` and/or `video.py` to create a video of what your model sees after the image is processed (may be helpful for debugging).
