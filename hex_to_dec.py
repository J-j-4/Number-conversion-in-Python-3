def hex_to_dec(hex_num):
    """Convert hexadecimal number to a decimal number"""
    dec_num = 0
    power = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for digit in hex_num[::-1]:
        dec_num += 16 ** power * digits.index(str(digit).upper())
        power += 1
    print(dec_num)

hex_to_dec('a')
hex_to_dec('1a')
hex_to_dec('2a')
