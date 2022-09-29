d = int(input('d-> '))
x = 3.14
print('s\np')
op = input('->')
res = ''

if op == 's':
    res = int(x*d*d)

if op =='p':
    res = int(x+d+2)

print(f'res = {res}')