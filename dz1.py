first = int(input('first nomber: '))
second = int(input('second numder: '))
text = str(first)
i = first
while second >= i:
    i += 1
    text += ' '
    text += str(i)
print('between nombers:', text)
