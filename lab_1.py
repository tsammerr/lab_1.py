n = int(input('number -> '))
c = int(input('cost -> '))
d = int(input('discount% -> '))
op = '->'
res = ''
print('1 -- total cost\n2 -- discounted price of one')


if op == '2':
    res = int(n - (d*c/100))

print(f'res = {res}')