n = int(input('number -> '))
c = int(input('cost -> '))
d = int(input('discount% -> '))
print('1 -- total cost\n2 -- discounted price of one')

op = input('-> ')
res = ""


if op == '1':
    res = int(n*(c - (d * c / 100)))


if op == '2':
    res = int(c - (d*c/100))

print(f'res = {res}')