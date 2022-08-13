import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001

button = Button.right

start_stop_key = KeyCode(char = 'a')
