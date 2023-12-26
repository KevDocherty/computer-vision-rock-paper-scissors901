# Computer Vision RPS

## Description
The module 'manual_rps.py' contains functions to allow the user to play a game of
'rock-paper-scissors' against the computer, and also calls those functions to
run the game. This involves the user making a choice from 'rock', 'paper', 'scissors'
from the command line, and the computer making a random choice from the same options.

The module 'camera_rps.py' offers the same functionality as manual_rps.py, except
in that it determines the user's choice via the web-cam, using a keras model
(keras_model.h5) which the user trained using Teachable Machine
(https://teachablemachine.withgoogle.com/). The user makes their choice by holding
up the corresponding item to the camera.

## Installation instructions
Save the modules 'manual_rps.py' and 'camera_rps.py', along wth the keras model files
(keras_model.h5, labels.txt) to a desired local folder.

## Usage instructions
Run the game from the command line, via:
> 'python manual_rps.py'
or
> 'python camera_rps.py'

## File structure of the project
The files necessary to play the game, are contaied in the root folder. Incidental
files used during development, are saved to the folder './other'
.
├── Keras_model.py
├── README.md
├── camera_rps.py
├── keras_model.h5
├── labels.txt
├── manual_rps.py
├── other
│   ├── OpenCV_Keras.py
│   ├── RPS-Template.py
│   └── requirements_rock-paper-scissors.txt
├── requirements.txt
└── requirements_rps_game.txt

## License information
n/a
