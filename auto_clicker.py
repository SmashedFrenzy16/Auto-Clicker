import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001

button = Button.right

start_stop_key = KeyCode(char = 'a')

stop_key = KeyCode(char = 'b')

class clickMouse(threading.Thread):

    def __init__(self, delay, button):

        super(clickMouse, self).__init__()

        self.delay = delay

        self.button = button

        self.running = False

        self.program_running = True

        def startClicking(self):

            self.running = True

        def stopClicking(self):

            self.running = True



