n = int(input('number -> '))
c = int(input('cost -> '))
d = int(input('discount% -> '))
print('1 -- total cost\n2 -- discounted price of one')

op = input('->')
res = ""


if op == '1':
    print('23')


if op == '2':
    res = int(n - (d*c/100))

print(f'res = {res}')