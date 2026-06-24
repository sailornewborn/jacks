from pygame import *


class ExtensibleGame:
    def __init__(self, window_size: tuple = (1280 / 2, 720 / 2)):
        init()
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.screen = display.set_mode((self.window_width, self.window_height))
        self.running = True

    def logic(self):
        self.screen.fill([255] * 3)
        display.flip()

    def event_handler(self, e: event.Event):
        if e.type == QUIT:
            self.running = False

    def run(self):
        while self.running:
            for e in event.get():
                self.event_handler(e)
            self.logic()
        quit()
