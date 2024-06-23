# 1

def get_char(c):
    return chr(c)

# 2

def divisible_by(numbers, divisor):
    result =[]
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result

# 3

def capitalize(s):
    result1 = ""
    result2 = ''
    for i,element in enumerate(s):
        if i % 2 == 0:
            result1 += element.upper()
            result2 += element.lower()
        else:
            result1 += element.lower()
            result2 += element.upper()
    return [result1, result2]

# 4

def min_sum(arr):
    arr.sort()
    min_sum = sum(arr[i] * arr[-i-1] for i in range(len(arr)// 2))
    return min_sum

# 5

def sum_consecutives(lst):
    result = []
    last_elem = None
    for i in lst:
        if i != last_elem:
            result.append(i)
            last_elem = i
        else:
            result[-1] += i
    return result

# 6

def parts_sums(ls):
    sum1 = sum(ls)
    list_of_sums = [sum1]
    for i in ls:
        sum1 = sum1 - i
        list_of_sums.append(sum1)
    return list_of_sums


# 7

def abreviator(word):
    if len(word) <= 3:
        return word
    return f"{word[0]}{len(word)- 2}{word[-1]}"

def abbreviate(s):
    result = []
    
    word = ""
    
    for i in s:
        if i.isalpha():
            word += i
        else:
            if word:
                result.append(abreviator(word))
                word = ""
            result.append(i)
    if word:
        result.append(abreviator(word))
        
    return "".join(result)

# 8

def solution(array_a, array_b):
    result = 0
    for i in range(len(array_a)):
        diff = array_a[i] - array_b[i]
        result = diff**2 + result
    final_result = result / len(array_a)
    
    return final_result


# 9

def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False
    sum = 0
    
    for i in range(9):
        if isbn[i].isdigit():
            sum += int(isbn[i]) * (i + 1)
        else:
            return False
    
    if isbn[9] == 'X':
        sum += 100
    elif isbn[9].isdigit():
        sum += int(isbn[9]) * 10
    else:
        return False
    
    return sum % 11 == 0

# 10

import math
def lcm(*args):
    return math.lcm(*args)
    


# 11

def format_duration(seconds):
    year = 365 * 24 * 3600
    day = 24 * 3600
    hour = 3600
    minute = 60
    
    if seconds == 0:
        return 'now'
    
    dict = [
        ["year", year],
        ["day", day],
        ["hour", hour],
        ["minute", minute],
        ["second", 1],
    ]
    
    result = []
    
    for name, time in dict:
        divided = seconds // time
        if divided > 0:
            if divided == 1:
                result.append(f"{divided} {name}")
            elif divided > 1:
                result.append(f"{divided} {name}s")
            seconds %= time
    
    if len(result) > 1:
        strn = ", ".join(result[:-1])
        return strn + ' and ' + result[-1]
    return result[0]