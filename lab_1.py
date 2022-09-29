sec = int(input('seconds -> '))
print('h - hours\nm - minutes\ns - seconds\nfull - full time')
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


if op == 'full':
    end = 86400
    between = end-sec
    print(f'ur time:{int(sec/3600)}: {int(sec%3600/60)}:{int:((sec%3600)%60)}')



#(f'{int(input(86400 - sec)/60)} minutes')

#(f'{int(86400 - sec)/60} minutes')



#end = 86400
#   between = end-sec

#if between > 0:
#  h = int(between/3600)
#  m = int(between % 3600/60)
#  s = int(between%3600%60)
#print(f'Left time: {h}:{m}:{s}')

