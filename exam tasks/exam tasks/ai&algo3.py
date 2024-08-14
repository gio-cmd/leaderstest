# Write python program that will turn decimal number into binary number.

# Test Cases:
# 32 -> 100000
# 31 -> 11111
# 8 -> 1000


def race_changer(num):
    if num == 0:
        return '0'
    
    result = ''

    while num != 0:
        result = str(num % 2) + result 
        num = num // 2

    return result


print(race_changer(8))