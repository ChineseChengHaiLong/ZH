def jia (a,b):
    return a+b
def jian (a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
aa=input("请输入您要计算的第一个数字:")

while True:
    if aa.replace(".",'').isdigit():
        if (aa.count(".")==0 or aa.count(".")==1) and aa.strip(".") == aa:
            aa = float(aa)
            print('OK')
            break
        else:
            aa = input('格式错误2，请重新输入：')
    else:
        aa = input('格式错误1，请重新输入：')
while True:
    bb=input('请输入要记算得方式(+, -, *, /),退出请按q键:')
    if bb == '+' or bb == '-' or bb == '*' or bb == '/':
        cc=input('请输入另一个数字:')
        
        while True:   
            if cc.replace(".",'').isdigit():
                if (cc.count(".")==0 or cc.count(".")==1) and cc.strip(".") == cc:
                    cc = float(cc)
                    print('OK')
                    break
                else:
                    cc = input('格式错误2，请重新输入：')
            else:
                cc = input('格式错误1，请重新输入：')
        if bb == '+':
            dd=jia(aa,cc)
            print(dd)
        elif bb == '-':
            dd=jian(aa,cc)
            print(dd)
        elif bb =='*':
            dd=cheng(aa,cc)
            print(dd)
        elif bb == '/':
            dd=chu(aa,cc)
            print(dd)
        aa=dd
    elif bb == 'q':
        break
    else:
        print('错误操作，请重新输入')
