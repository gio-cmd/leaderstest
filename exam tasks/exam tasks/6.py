# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Test Cases:
# 'Pig latin is cool' -> 'igPay atinlay siay oolcay'
# 'This is my string' -> 'hisTay siay ymay tringsay'
# "Ultima necat" -> 'ltimaUay ecatnay'
# "Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
# "Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'


def ayay(word):
    list = word.split()
    result = []

    for i in list:
        if not i.isalpha():
            result.append(i)
        else:
            result.append(i[1:] + i[0] + 'ay')
    
    return " ".join(result)

print(ayay('TCucullus non facit monachum'))
