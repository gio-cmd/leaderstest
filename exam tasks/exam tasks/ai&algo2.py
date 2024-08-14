# Write an algorithm in python to count the number of capital letters in
# a string. How many comparisons does it do? What is the fewest num-
# ber of increments it might do? What is the largest number? (Use N for the
# number of characters in the file when writing your answer.)

def capital_counter(strng):
    count = 0

    for i in strng:
        if i == i.upper():
            count += 1

    return count

# 1. N (we dont care if its lower or upper we still gota compare them)
# 2. 0 if there are no upper letters
# 3. N if whole inputed string is made out of upper letters