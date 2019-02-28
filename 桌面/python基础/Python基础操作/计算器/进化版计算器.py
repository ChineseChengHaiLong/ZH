def He(b,c):
    return b+c
def Cha(b,c):
    return b-c
def Ji(b,c):
    return b*c
def Shang(b,c):
    return b/c

aa = input('请输入第一个数字')
while True:
    try:
        aa = float(aa)
        print(type(aa))
        break
    except:
        aa = input('错误操作，请重新输入：')

while True:
    bb=input('请输入要记算得方式(+, -, *, /),退出请按q键:')
    if bb == '+' or bb == '-' or bb == '*' or bb == '/':
        cc=input('请输入另一个数字:')
        while True:
            try:
                cc = float(cc)
                print(type(cc))
                break
            except:
                cc = input('c错误操作，请重新输入：')        
        if bb == '+':
            dd=He(aa,cc)
            print(dd)
        elif bb == '-':
            dd=Cha(aa,cc)
            print(dd)
        elif bb =='*':
            dd=Ji(aa,cc)
            print(dd)
        elif bb == '/':
            dd=Shang(aa,cc)
            print(dd)
        aa=dd
    elif bb == 'q':
        break
    else:
        print('1错误操作，请重新输入')    
