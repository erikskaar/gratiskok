import re
D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
80: 'eighty', 90: 'ninety'}

L = [ 1000000, ' million', 1000, ' thousand', 1, '']


def i2_txt(value):
    if 1 <= value <= 99:
        if D.get(value) == None:

            result = D.get(value//10*10) + '-' + D.get(value%10)
            return result
        else:
            return D.get(value)
    else:
        return 'Too big or too small number'

#print(i2_txt(82))


def i3_txt(value):
    if 100 <= value <= 999:
        rest = value%100
        if D.get(value) == None:
            if rest != 0:
                result = D.get(value//100) + ' hundred ' + i2_txt(rest)
            else:
                result = D.get(value//100) + ' hundred'
            return result
        else:
            return i2_txt(value)
    elif 1 <= value <= 99:
        return i2_txt(value)

#print(i3_txt(100))


def i9_txt(value):
    return '[INSERT NUMBER HERE]'

def add_words(sentence):

    workSen = sentence.split()
    for x in range(len(workSen)):
        try:
            num = int(workSen[x])
            workSen[x] += ' - ' + i9_txt(workSen[x]) + ' -'
        except:
            pass
    return ' '.join(workSen)
print(add_words('hey 52 there 929229'))