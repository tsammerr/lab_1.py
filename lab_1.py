sec = int(input('seconds -> '))
print('h - hours\nm - minutes\ns - seconds')
op = input('=> ')
res = ""

if op == 'h':
    res = (f'{int(((86400 - sec)/3600))} hours')
    print(f'res = {res}')

if op =='m':
    res = (f'{int((86400 - sec)/60)} minutes')
    print(f'res = {res}')

if op =='s':
    res = (f'{int((86400 - sec))} seconds')
    print(f'res = {res}')
