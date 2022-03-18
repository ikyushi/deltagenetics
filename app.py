from plistlib import load
from pathlib import Path
import os
import time
import random
import math
import json
from topLevelFunctions import *

replay = True

inventory = []

clear()
strobeText("DELTAGENETICS", 0.5, 10)
strobeText("by simplesentai", 0.5, 10)
print("Press [ENTER] to begin...")
input()
clear()
while replay == True:
    hasPlayed = input("Have you played this game before? (y/N) ")
    if hasPlayed.lower() == "y":
        pass
    else:
        print("Welcome to DELTAGENETICS!")
        print("This game is a text-based, story-driven adventure game.")
        print("You will be able to explore Delta, a futuristic world of mystery, danger, and endless possibilities.")
        print("You will be able to interact with objects and people in the world, and you will be able to learn about our world.")
        print("However, you are unable to save the 'game', as life simply doesn't work like that.")
        print("If you have to close the game, you will lose all progress and be returned here.")
        print("Good luck!")
        input("Press [ENTER] to begin...")
        clear()
        pass
    printstory("It happened again.")
    printstory("Last night, you felt a strange sensation in your chest.")
    printstory("Almost as if you were being watched.")
    printstory("You were in a room, and you were alone.")
    printstory("On that table, there were four small boxes.")
    printstory("But... something feels off...")
    printstory("You can't quite remember which box you opened.")
    print("Which one did you open? (1, 2, 3, or 4)")
    box = input()
    if box == "1":
        printstory("Ah yes, you remember now. You opened the first box.")
        printstory("It was a small, black box.")
        printstory("Inside, there was a small, red button, which you pressed.")
        printstory("You felt the ground shake underneath you.")
        printstory("That must be good, right?")
    elif box == "2":
        printstory("You opened the second box.")
        printstory("It was a small, blue box.")
        printstory("Inside that box, there was a small key.")
        printstory("Obviously, you picked up the key, as you thought that it might become useful.")
        inventory.append("room1.key")