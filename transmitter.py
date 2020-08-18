from signal_maker import Signal_Maker
from signal import Signal


class Transmitter:
    def __init__(self):
        pass

    def send_signal(self, signal):
        Signal_Maker().make_signal(signal)


signal = Signal("01100")
Transmitter().send_signal(signal)
