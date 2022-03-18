import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def delayClear(delay):
    time.sleep(delay)
    clear()

def wait(delay):
    time.sleep(delay)

def strobeText(text, delay, repeat):
    for i in range(repeat):
        print(text)
        delayClear(delay)
        wait(delay)

def printstory(content):
    print(content)
    input()