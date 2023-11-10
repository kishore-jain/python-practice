print('Task-1')
print('odious or evile number methods')
print('---------------------------')

num = int(input('enter the number : '))

s = bin(num)

a = str(s)

b =a.count("1")
if(b % 2 ==0):
    print("Evil number")
else:
    print("odious number")
