
import os   # 用来进行文件操作以及 执行cmd命令
import time # 时间上的操作，以及 手动延迟

'''
_____提款机系统_____
功能介绍 ：
1. 查看余额
2. 提出款项
3. 存入款项
4. 查看记录
'''
# 定义 户口上的金额数量
my_money = 200

def save_action(action, money_amount):  # 接收两个参数 ：动作（提出/存入），金额数量
    with open('Log.txt','a',encoding='utf-8') as f:
        # 时间戳
        t = time.strftime(r'%Y-%m-%d | %H:%M:%S')

        f.write(
            '您于'+ t + action + '了' + str(money_amount) + ' 元'+ '\n'
        )

def check_money():  # 查看余额
    print('_____正在进行操作 ：查看余额_____')

    global my_money

    print(f'当前您的户口上有{my_money} 元哦 ~')

def get_money():    # 提出款项
    print('_____正在进行操作 ：提出款项_____')
    global my_money

    # 提供输入框，让用户输入想要提出的金额数量
    money_amount = int(input(f'请您输入想要提出的金额数量(当前户口上有{my_money} 元) ：'))

    # 进行判断
    if money_amount > my_money :
        print('您的户口上没有那么多钱哦 ~')

        save_action('无法提出', money_amount)

    else :  # 成功提出款项
        # 自减
        my_money -= money_amount    # my_money = my_money - money_amount

        print(f'您成功提出{money_amount}了，户口上还剩下{my_money} 元')

        # 记录操作
        save_action('提出', money_amount)


def save_money():   # 存入款项
    print('_____正在进行操作 ：存入款项_____')
    global my_money

    # 提供输入框，让用户输入想要存入的款项数量
    money_amount = int(input(f'请输入您想要存入的金额数量(当前户口上有{my_money} 元) ：'))

    # 自增
    my_money += money_amount    # my_money = my_money + money_amount

    print(f'成功存入{money_amount} 元，当前户口上有{my_money} 元 ~')

    # 记录操作
    save_action('存入', money_amount)

def check_history():    # 查看记录
    print('_____正在进行操作 ：查看记录_____')
    global my_money

    try :
        with open('Log.txt','r',encoding='utf-8') as f:
            history_list = f.readlines()
        
        # 计算多少条记录
        counter = 1
        
        for i in history_list :
            print(counter , i.replace('\n',''))

            # 自增
            counter += 1
    except :    # 报错后的处理
        print('您还没有操作记录，请进行操作后才来查看记录')


if __name__ == '__main__' : # 当我们在当前文件运行程序的话，才会运行这块
    while True :
        # 清空cmd记录
        os.system('cls')

        # 打印标题
        print('''
        .----------------.  .----------------.  .----------------. 
        | .--------------. || .--------------. || .--------------. |
        | |      __      | || |  _________   | || | ____    ____ | |
        | |     /  \     | || | |  _   _  |  | || ||_   \  /   _|| |
        | |    / /\ \    | || | |_/ | | \_|  | || |  |   \/   |  | |
        | |   / ____ \   | || |     | |      | || |  | |\  /| |  | |
        | | _/ /    \ \_ | || |    _| |_     | || | _| |_\/_| |_ | |
        | ||____|  |____|| || |   |_____|    | || ||_____||_____|| |
        | |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------' 
        ''')

        
        # 提供用户功能选项输入框
        print('''
        1. 查看余额
        2. 提出款项
        3. 存入款项
        4. 查看记录
        ''')
        opt = input('请输入您的功能选项 ：')

        # 进行判断 处理
        if opt == '1' : # 查看余额
            check_money()
        elif opt == '2' :   # 提出款项
            get_money()
        elif opt == '3':    # 存入款项
            save_money()
        elif opt == '4':    # 查看记录
            check_history()
        else :  # 当用户输入的结果，不在功能选项范围内，
            print('选项只有 1 到 4，请输入正确的选项 ！')
            time.sleep(2)   # 手动延迟两秒
            continue    # 重复循环

        # 是否继续进行其他操作 ？
        con = input('是否想要继续进行其他操作?(y/n)')   # y --> yes ：继续操作 | n --> no ：不继续操作，退出程序

        if con == 'y' :
            continue    # 继续循环
        elif con == 'n' :
            break   # 退出死循环，程序就会退出了
        else :  # 用户输入的结果不是 'y' 也不是 'n'的时候，默认退出程序
            print('您输入的结果不在操作选项内，程序默认为您退出程序 ~')
            break


