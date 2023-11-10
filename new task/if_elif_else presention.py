print('Present of DMS')
print('--------------')
print('if...elif...else is 3rd condition of DMS')
print('-----------------------------------------')
print(' find the lergest number if...elif...else')
print('---------------------------------------')


a =int(input('enter a 1st number: '))
b =int(input('enter a 2nd number: '))
c =int(input('enter a 3rd number: '))

if a>b and a>c:
    print('1st value is greater')
elif b>a and b>c:
    print('2nd value is greater')
elif c>a and c>b:
    print ('3rd value is greater')
else:
    print('all values is same')
