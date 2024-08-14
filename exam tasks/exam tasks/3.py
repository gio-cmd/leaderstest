# You will be given a number and you will need to return it as a string in Expanded Form

# Test Cases:
# 70304 -> '70000 + 300 + 4'
          # 70000 + 300 + 4
# 42 -> '40 + 2'
# 710163 -> '700000 + 10000 + 100 + 60 + 3'
          #  700000 + 10000 + 100 + 60 + 3
# 853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
            #800000 + 50000 + 3000 + 500 + 40 + 6 
# 511604 -> '500000 + 10000 + 1000 + 600 + 4'
#            500000 + 10000 + 1000 + 600 + 4


def expander(num):
    str_num = str(num)
    result = []

    count = len(str_num)

    for i in str_num:
        if i != '0':
            result.append(i + '0' * (count - 1))
        count -= 1

    return ' + '.join(result)

print(expander('511604'))