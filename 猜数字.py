number=input('请输入需要猜的数字:')
while True:
    guess=input('猜猜0-10:')
    if guess>number:
        print('太大了')
    elif guess<number:
        print('太小了')
    else:
        print('right!')
        break