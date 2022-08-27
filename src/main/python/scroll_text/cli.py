from time import sleep
from enum import Enum
from l2term import Lines
from colorama import init as colorama_init
from colorama import Style
from colorama import Fore


class Speed(Enum):
    NORMAL = .07
    FAST = .03
    SLOW = .11


class Marquee(object):

    def __init__(self, message=None, speed=Speed.NORMAL, size=None, use_color=True):
        """ initialize Marquee
        """
        self.use_color = use_color
        if use_color:
            colorama_init()
        if not isinstance(speed, Speed):
            raise ValueError("speed must be an instance of Speed Enum")
        self.speed = speed
        self.size = size
        self._feed = self.size * ' ' + message
        self._start()

    def _get_message(self, start):
        """ return message to display
        """
        if self.use_color:
            return f"{Fore.YELLOW}{self._feed[start:start + self.size]}{Style.RESET_ALL}"
        return self._feed[start:start + self.size]

    def _start(self):
        """ start the text marquee
        """
        with Lines(size=1, show_index=False) as lines:
            try:
                start = 0
                while True:
                    if start == len(self._feed):
                        start = 0
                    lines[0] = self._get_message(start)
                    start += 1
                    sleep(self.speed.value)
            except KeyboardInterrupt:
                lines.clear()


message = "I love the design of the watch and I think they did a great job with the UI considering the limited screen. I'm curious how fast Casio would roll out updates to this and how friendly it would work with third party devices and software in the future."
Marquee(message=message, size=100)
