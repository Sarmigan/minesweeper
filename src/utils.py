def get_digits(number):
    units = number % 10
    tens = (number // 10) % 10
    hundreds = number // 100

    return hundreds, tens, units