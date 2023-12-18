"""
This module contains the functions to play a game of 'rock-paper-scissors',
and calls said functions so that a user can play against the computer
"""

from random import randint

def get_computer_choice():
    """
    This function makes and returns a random choice from 'rock', 'paper', 'scissors'
    """
    choices = ['rock', 'paper', 'scissors']
    return choices[randint(0,2)]

def get_user_choice():
    """
    This function asks the user to make a choice from 'rock', 'paper', 'scissors',
    and then returns that choice
    """
    choice = input("Make your choice: rock(r), paper(p), or scissors(s): ")
    if choice == 'r':
        return 'rock'
    if choice == 'p':
        return 'paper'
    return 'scissors'

def get_winner(computer_choice, user_choice):
    """
    This function compares the choices of the user and the computer
    and prints a message to let the user know the result of the game.

    It returns nothing.
    """
    if (computer_choice == 'rock' and user_choice == 'scissors'):
        print("You lost")

    elif (computer_choice == 'rock' and user_choice == 'rock'):
        print("It is a tie!")

    elif (computer_choice == 'scissors' and user_choice == 'paper'):
        print("You lost")

    elif (computer_choice == 'scissors' and user_choice == 'scissors'):
        print("It is a tie!")

    elif (computer_choice == 'paper' and user_choice == 'paper'):
        print("It is a tie!")

    elif (computer_choice == 'paper' and user_choice == 'scissors'):
        print("You won!")

    elif (computer_choice == 'rock'and user_choice == 'paper'):
        print("You won!")

    elif (computer_choice == 'paper' and user_choice == 'rock'):
        print("You lost")

    elif (computer_choice == 'scissors' and user_choice == 'rock'):
        print("You won!")
    else:
        print("This is not a valid object selection.")

def play():
    """
    This function calls the other functions to play a game of rock-paper-scissors
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()
