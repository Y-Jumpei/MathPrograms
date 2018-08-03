print '---CollatzProblem---'

Num = input('>> ')
Count = 0
print Num,
while Num != 1:
    Count += 1
    print '->',
    if Num % 2 == 0:
        Num = Num / 2
    else:
        Num = 3 * Num + 1
    
    if Count % 10 == 0:
        print Num
    else:
        print Num,
print '\nCount = {}'.format(Count)


