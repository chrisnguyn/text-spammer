import pyautogui  # pip3 install -r requirements.txt
import time  # don't need to install this -- comes with Python IIRC

# IMPORTANT NOTICE:
# TO ALL MY FRIENDS THAT WILL USE THIS SCRIPT, KNOW HOW TO ABORT IT BEFORE YOU START IT UP
# THIS WILL LITERALLY GO ON FOREVER UNTIL YOU MANUALLY STOP IT. DON'T CLICK OUTSIDE OF THE MESSAGES BOX!

script = 'whatever you write in here will be sent word by word'

input('PRESS ENTER TO UNLEASH HELL')
print('3!')
time.sleep(1)
print('2!')
time.sleep(1)
print('1!')
time.sleep(1)

while True:
    for word in script.split():  # split string by spaces into a list; this types each word as opposed to each letter
        pyautogui.write(word)
        pyautogui.press('enter')