#break
x = 0
while x<10:
    print('x is currently:',x)
    print('x is still less than 10,adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')