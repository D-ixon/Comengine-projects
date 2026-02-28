a = float(input('First number: '))
b = float(input('Second number: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')
