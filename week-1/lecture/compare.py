x = int(input('Whats x?: '))
y = int(input('Whats y?: '))

if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')

if x < y or x > y:
    print('x is not equal to y')
else:
    print('x is equal to y')

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greter than y')
else:
    print('x and y are equal to each other')
