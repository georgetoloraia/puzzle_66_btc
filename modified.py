import random
from bitcoin import privtopub, compress, pubtoaddr

class Main:
    def __init__(self, bit_max, bit_min, shua):
        self.bit_max = bit_max
        self.bit_min = bit_min
        self.shua = shua

class Calculate(Main):
    def __init__(self, bit_max, bit_min, shua):
        super().__init__(bit_max, bit_min, shua)

    def calculation(self):
        while True:
            i = random.randint(self.bit_min, self.bit_max)
            priv_dec_float = i
            priv_decimal = hex(priv_dec_float)[2:]
            private = priv_decimal.zfill(16).rjust(64, '0') # aq 0ebit sheivseba
            my_private_key = private
            my_public_key = privtopub(my_private_key) # es amushavebs da gardaqmnis public key-d
            my_compressed_public_key = compress(my_public_key) #,shesakumshad' anu ufro mokled warmosadgenad
            my_address = pubtoaddr(my_compressed_public_key)

            if my_address.startswith("13zb1hQ"):
                print(f"btc_address is: {my_address}\nprivatekey_in_hex is: {my_private_key}\ndecimal is: {i}")
                print("now recalculating decimal / 2")

            if i > self.shua:
                if i % 2 != 0:
                    self.bit_min = i + 1
                    print("\n--------------------------\n")
                    print(f"new MIN decimal is: {self.bit_min}")
                    calculate_max = self.bit_max - i
                    if calculate_max % 2 != 0:
                        calculate_max = round((calculate_max + 1) / 2)
                        self.shua = calculate_max
                    else:
                        calculate_max = calculate_max // 2
                        self.shua = calculate_max
            else:
                self.bit_min = i
                print("\n--------------------------\n")
                print(f"new MIN decimal is: {self.bit_min}")
                calculate_max = self.bit_max - i
                if calculate_max % 2 != 0:
                    calculate_max = round((calculate_max + 1) / 2)
                    self.shua = calculate_max
                else:
                    calculate_max = calculate_max // 2
                    self.shua = calculate_max

            if my_address == "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so":
                print(f"decimal: {i}, private: {my_private_key}, address: {my_address}")
                break

bit_max = 73786976294838206464
bit_min = 36893488147419103232
shua = 55340232221128654848

calculator = Calculate(bit_max, bit_min, shua)
calculator.calculation()