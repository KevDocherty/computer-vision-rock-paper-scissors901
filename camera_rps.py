"""
This module contains the functions required to play a game of 'rock-paper-scissors',
using computer vision to recognise the user's gestures,
and calls said functions so that a user can play against the computer
"""

# load the required libraries
import cv2
from keras.models import load_model
import numpy as np
from random import randint

def get_prediction():
    """
    This function uses a Keras model, created using Teachable Machine,
    to recognise whether the user's hand is indicating rock, paper, or scissors
    """
    # load the computer vision model
    #model = load_model('keras_model.h5', compile=True)
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)

    # 'data' = 4-dimensional numpy array:
    # - the first dimension represents the number of samples in the array,
    # which is 1 in this case
    # - the second and third dimensions represent the height and width of the image,
    # which are both 224 pixels.
    # - the fourth dimension represents the number of color channels in the image,
    # which is 3 (red, green, and blue)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # create an empty np array to append each prediction as a separate row
    predictions = np.ndarray(shape=(1, 4))

    # collect an np.array of 50 rows x 4 columns,
    # where each row element is a float representing the probability of
    # rock, paper, scissors, nothing, respectively
    for i in range(50):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window

        # debug statements...
        #print(type(prediction))
        #print(prediction.shape)

        print(np.round(prediction[0],2))
        # append each 'prediction' to 'predictions'
        if i == 0:
            predictions = prediction
        else:
            predictions = np.vstack([np.round(prediction[0],2), predictions])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # debug statements
    #print(predictions)
    #print(np.sum(predictions, axis=0))

    # sum each column of predictions, and return the most probable result
    # according to which has the maximum value
    totals = np.sum(predictions, axis=0)
    if np.argmax(totals) == 0:
        #print('rock')
        return 'rock'
    elif np.argmax(totals) == 1:
        #print('paper')
        return 'paper'
    elif np.argmax(totals) == 2:
        #print('scissors')
        return 'scissors'
    else:
        #print('nothing')
        return 'nothing'

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_computer_choice():
    """
    This function makes and returns a random choice from 'rock', 'paper', 'scissors'
    """
    choices = ['rock', 'paper', 'scissors']
    return choices[randint(0,2)]

def get_winner(computer_choice, user_choice):
    """
    This function compares the choices of the user and the computer
    and prints a message to let the user know the result of the game.

    It returns nothing.
    """
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("This is not a valid object selection.")
        return

    if computer_choice == 'rock':
        if user_choice == 'scissors':
            print("You lost")
        elif user_choice == 'paper':
            print("You won!")
        elif user_choice == 'rock':
            print("It is a tie!")

    if computer_choice == 'paper':
        if user_choice == 'scissors':
            print("You won!")
        elif user_choice == 'paper':
            print("It is a tie!")
        elif user_choice == 'rock':
            print("You lost")

    if computer_choice == 'scissors':
        if user_choice == 'scissors':
            print("It is a tie!")
        elif user_choice == 'paper':
            print("You lost")
        elif user_choice == 'rock':
            print("You won!")

def play():
    """
    This function calls the other functions to play a game of rock-paper-scissors
    """
    computer_choice = get_computer_choice()
    print(f"The computer's choice is: {computer_choice}")
    #user_choice = get_user_choice()
    user_choice = get_prediction()
    print(f"The user's choice is: {user_choice}")
    get_winner(computer_choice, user_choice)

if __name__ == '__main__':
    play()
