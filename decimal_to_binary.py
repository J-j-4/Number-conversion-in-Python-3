# Convert Decimal number to Binary Number


def dec_to_bin(dec_num):
    """Convert Decimal Number dec_num to Binary Number"""
    bin_num = 0
    power = 0
    while dec_num > 0:
        bin_num += 10 ** power * (dec_num % 2)
        dec_num //= 2
        power += 1
    return bin_num

print(dec_to_bin(46))
