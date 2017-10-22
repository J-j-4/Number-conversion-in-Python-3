# Convert any number base to another base
# Developed by Md. Mohaymenul Islam (Noyon)

def num_convert(from_number, from_base, to_base):
    """Convert from_number to another base number."""
    to_number = 0
    power = 0
    while from_number > 0:
        to_number += from_base ** power * (from_number % to_base)
        from_number //= to_base
        power += 1
    return to_number

print(num_convert(101110, 2, 10))
print(num_convert(46, 10, 2))
print(num_convert(46, 10, 8))
print(num_convert(30, 10, 2))
print(num_convert(111000111, 2, 8))
