Num = input('>> ')
Count = 0
for i in range(2,Num):
    if Num % i == 0:
        print '{} is not Prime Number'.format(Num)
        break
else:
    print '{} is Prime Number.'.format(Num)