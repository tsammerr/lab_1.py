x = int(input('time -> '))

res = ""

if x >= 6 and x < 13 :
    print('Good Morning:)')

if x >= 13 and x < 17:
    print('Good Day:)')

if x >= 17 and x <= 23:
    print('Good Evening:)')

if x >= 0 and x < 6:
    print('Good Night:)')

else:
    print('Error!')
