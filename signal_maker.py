from graphics import *
from time import sleep


class Signal_Maker:
    def __init__(
        self,
        signal_start_color="blue",
        bit_start_color="yellow",
        on_bit_color="green",
        off_bit_color="red",
        interim_time=0.1,
        bit_duration=1,
    ):
        self.signal_start_color = signal_start_color
        self.bit_start_color = bit_start_color
        self.on_bit_color = on_bit_color
        self.off_bit_color = off_bit_color
        self.interim_time = interim_time
        self.bit_duration = bit_duration

    def make_signal(self, signal, width=1300, height=700):
        win = GraphWin("Signal Window", width, height)
        rect = Rectangle(Point(0, 0), Point(width, height))
        rect.draw(win)
        rect.setFill(self.signal_start_color)
        sleep(self.bit_duration)
        for bit in signal.signal:
            rect.setFill(self.bit_start_color)
            sleep(self.interim_time)
            if bit == "1":
                rect.setFill(self.on_bit_color)
            else:
                rect.setFill(self.off_bit_color)
            sleep(self.bit_duration)
        rect.setFill(self.bit_start_color)
        sleep(self.bit_duration)
        rect.setFill(self.signal_start_color)
        sleep(self.bit_duration)
        win.close()
