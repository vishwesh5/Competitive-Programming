import math
def get_count_digits(number):
    """Return number of digits in a number."""

    if number == 0:
        return 1

    number = abs(number)

    if number <= 999999999999997:
        return math.floor(math.log10(number)) + 1

    count = 0
    while number:
        count += 1
        number //= 10
    return count
print(get_count_digits(int(input().strip())+1))
