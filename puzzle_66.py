
# # # full bit 50% / 50%
# # a = 73786976294838206464-36893488147419103232 # rezult is: 36893488147419103232
# # b = "{:.19f}".format(a)
# # print(b)

# # s1 = 36893488147419103232 / 2  # rezult is: 18446744073709551616
# # s2 = "{:.19f}".format(s1)
# # print(s2)

# max = 36893488147419103232 + 18446744073709551616 # rezult is 55340232221128654848
# max50 = "{:.0f}".format(max)
# print(f"min plius = :  {max50}")

# min = 73786976294838206464 - 18446744073709551616  # rezult is 55340232221128654848
# min50 = "{:.0f}".format(min)
# print(f"max minus = :  {min50}")

# from bitcoin import privkey_to_address
import random
from bitcoin import *

bit_max = 73786976294838206464
bit_min = 36893488147419103232
shua = 55340232221128654848

def decimal_calculate():
    bit_max = 73786976294838206464
    bit_min = 36893488147419103232
    shua = 55340232221128654848
    # for i in range(random.randint(bit_min, bit_max)):
    while True:
        bit_max = 73786976294838206464
        bit_min = 36893488147419103232
        shua = 55340232221128654848
        i = random.randint(bit_min, bit_max)
        priv_dec_float = i
        priv_decimal = hex(priv_dec_float)[2:]
        private = priv_decimal.zfill(16).rjust(64, '0')
        my_private_key = private
        my_public_key = privtopub(my_private_key)
        my_compressed_public_key = compress(my_public_key)
        my_address = pubtoaddr(my_compressed_public_key)
        if my_address.startswith("13zb1hQ"):
            print(f"btc_address is : {my_address}")
            print(f"privatekey_in_hex is : {my_private_key}")
            print(f"decimal is : {i}")
            print("now recalculating decial / 2")
            if i > shua:
                if i % 2 != 0:
                    bit_min = i + 1
                    print("\n -------------------------- \n")
                    print(f"new MIN decimal is : {bit_min}")
                    calculate_max = bit_max - i
                    if calculate_max % 2 != 0:
                        calculate_max = calculate_max + 1
                        calculate_max = calculate_max / 2
                        calculate_max = "{:.0f}".format(calculate_max)
                        shua = calculate_max
                    else:
                        calculate_max = calculate_max / 2
                        calculate_max = "{:.0f}",format(calculate_max)
                        shua = calculate_max
                else:
                    bit_min = i
                    print("\n -------------------------- \n")
                    print(f"new MIN decimal is : {bit_min}")
                    calculate_max = bit_max - i
                    if calculate_max % 2 != 0:
                        calculate_max = calculate_max + 1
                        calculate_max = calculate_max / 2
                        calculate_max = "{:.0f}".format(calculate_max)
                        shua = calculate_max
                    else:
                        calculate_max = calculate_max / 2
                        calculate_max = "{:.0f}",format(calculate_max)
                        shua = calculate_max

            if i < shua:
                if i % 2 != 0:
                    bit_max = i + 1
                    print("\n -------------------------- \n")
                    print(f"new MAX decimal is : {bit_max}")
                    calculate_min = i - bit_min
                    if calculate_min % 2 != 0:
                        calculate_min = calculate_min + 1
                        calculate_min = calculate_min / 2
                        calculate_min = "{:.0f}".format(calculate_min)
                        shua = calculate_min
                    else:   
                        calculate_min = calculate_min / 2
                        calculate_min = "{:.0f}".format(calculate_min)
                        shua = calculate_min
                else:
                    bit_max = i
                    print("\n -------------------------- \n")
                    print(f"new MAX decimal is : {bit_max}")
                    calculate_min = i - bit_min
                    if calculate_min % 2 != 0:
                        calculate_min = calculate_min + 1
                        calculate_min = calculate_min / 2
                        calculate_min = "{:.0f}".format(calculate_min)
                        shua = calculate_min
                    else:   
                        calculate_min = calculate_min / 2
                        calculate_min = "{:.0f}".format(calculate_min)
                        shua = calculate_min
        if my_address == "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so":
            print("woooow....  privat gasagebi napovnia")
            print(f"decima: {i}   private : {my_private_key}  address : {my_address}")
            break

decimal_calculate()




