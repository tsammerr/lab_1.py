g = int(input('file size -> '))
s = int(input('internet speed -> '))

print('For loading this file u will need:\n1 -- hours\n2 -- minutes\n3 -- seconds')

op = input('-> ')
res = ""

if op == '1':
    res = int(((g*8589934592)/s)/3600)
    print(f'res = {res} hours')

if op == '2':
    res = int(((g*8589934592)/s)/60)
    print(f'res = {res} minutes')

if op == '3':
    res = int((g*8589934592)/s)
    print(f'res = {res} seconds')
