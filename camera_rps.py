"""
This module contains the functions required to play a game of 'rock-paper-scissors'
using computer vision to recognise the user's gestures,
and calls said functions so that a user can play against the computer
"""

# load the required libraries
import cv2
from keras.models import load_model
import numpy as np
from random import randint
import time

def get_prediction():
    """
    This function uses a Keras model, created using Teachable Machine,
    to recognise whether the user is holding up rock, paper, or scissors
    to the webcam.

    The user is presented with a countdown from 10, at the end of which
    the user must present their choice to the camera.
    """
    # load the computer vision model
    #model = load_model('keras_model.h5', compile=True)
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)

    # 'data' = 4-dimensional numpy array:
    # - the first dimension represents the number of samples in the array (1 in this case)
    # - the second and third dimensions represent the height and width of the image (both 224 pixels)
    # - the fourth dimension represents the number of color channels in the image, = 3 (red, green, and blue)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    t1 = time.time()
    countdown = 10
    count = []
    labels = ['rock', 'paper', 'scissors', 'nothing']

    while True:
        #countdown_displayed = False
        t2 = time.time()
        time_elapsed = t2 - t1
        if time_elapsed > countdown:
            print("time's up!")
            break
        if time_elapsed % 1 < 0.01 and int(time_elapsed) not in count:
            count.append(int(time_elapsed))
            #print(int(countdown - time_elapsed))
            print(f"Time remaining: {countdown - count[-1]} seconds")

            # capture an image from the webcam
            # and classify as rock, paper, or scissors
            # using the Keras model
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window

            user_choice = labels[np.argmax(prediction)]

            print(f"Your choice is: {user_choice}")
    #print(count)
    return(user_choice)

def get_computer_choice():
    """
    This function makes and returns a random choice from 'rock', 'paper', 'scissors'
    """
    choices = ['rock', 'paper', 'scissors']
    return choices[randint(0,2)]

def get_winner(computer_choice, user_choice):
    """
    This function compares the choices of the user and the computer
    and prints a message to let the user know the result of the game
    and returns the winner.
    """
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("This is not a valid object selection.")
        return

    winner = 'tie'
    if computer_choice == 'rock':
        if user_choice == 'scissors':
            print("You lost")
            winner = 'computer'
        elif user_choice == 'paper':
            print("You won!")
            winner = 'user'
        elif user_choice == 'rock':
            print("It is a tie!")

    if computer_choice == 'paper':
        if user_choice == 'scissors':
            print("You won!")
            winner = 'user'
        elif user_choice == 'paper':
            print("It is a tie!")
        elif user_choice == 'rock':
            print("You lost")
            winner = 'computer'

    if computer_choice == 'scissors':
        if user_choice == 'scissors':
            print("It is a tie!")
        elif user_choice == 'paper':
            print("You lost")
            winner = 'computer'
        elif user_choice == 'rock':
            print("You won!")
            winner = 'user'
    return winner

def play():
    """
    This function calls the other functions to play a game of rock-paper-scissors.
    It counts the number of wins for the user and the computer, such that the
    overall winner is the first to win 3 games
    """
    user_wins = 0
    computer_wins = 0
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_prediction()

        print(f"The computer's choice is: {computer_choice}")
        print(f"Your choice is: {user_choice}")
        winner = get_winner(computer_choice, user_choice)
        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1

        if computer_wins == 3:
            print('The computer wins!')
            break
        elif user_wins == 3:
            print('The user wins!')
            break




if __name__ == '__main__':
    play()
