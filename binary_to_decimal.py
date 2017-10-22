# Binary to Decimal Conversion


def binToDec(bin_num):
    """convert binNum to Decimal Number."""
    dec_num = 0
    power = 0
    while bin_num > 0:
        dec_num += 2 ** power * (bin_num % 10)
        bin_num //= 10
        power += 1
    return dec_num

print(binToDec(101110))

