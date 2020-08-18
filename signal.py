class Signal:
    def __init__(self, signal):
        self.signal = signal

    def error_bits_per_mod(self, modulus):
        number_of_bits = len(self.signal)
        error_bits = [0] * modulus
        for start in range(modulus):
            i = start
            while i < number_of_bits:
                if signal[i] == "1":
                    error_bits[start] += 1
                i += modulus
            error_bits[start] %= 2
        error_bits = "".join(map(str, error_bits))
        return error_bits

    def error_bits(self, modulos):
        net_error_bits = ""
        for modulo in modulos:
            net_error_bits.join(self.error_bits_per_mod(self.signal, modulo))
        return net_error_bits

    def get_encoded_signal(self, modulos):
        return Signal(self.signal + self.error_bits(modulos))

