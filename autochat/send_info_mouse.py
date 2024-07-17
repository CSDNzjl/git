import psutil
import time
import os
import pyperclip
import pyautogui as gui

# 判断QQ是否登录
QQ_dir = r'C:\Program Files\Tencent\QQNT\QQ.exe'
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:  # 通过PID判断
        if psutil.Process(pid).name() == process_name:
            return True
    return False

# 发送消息
def send_msg(people, msg):
    if not proc_exist('QQ.exe'):
        # 登录QQ
        QQ_login()

    # 搜索好友并打开聊天窗口
    gui.moveTo(280, 210, duration=0.2)
    gui.click()
    time.sleep(0.5)
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    print("输入1以继续：")
    if(input()=="1"):
        gui.moveTo(280, 210, duration=0.2)
        gui.click()
        gui.press('enter')
        time.sleep(1)

    # 输入需要发送的信息
    gui.moveTo(616, 774, duration=0.2)
    gui.click()
    pyperclip.copy(msg)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    print("输入1以继续：")
    if (input() == "1"):
        gui.moveTo(616, 774, duration=0.2)
        gui.click()
        gui.press('enter')

# 登录QQ
def QQ_login():
    os.startfile(QQ_dir)
    print('正在打开QQ')
    time.sleep(3)
    gui.moveTo(960, 695, duration=0.5)
    gui.click()
    time.sleep(10)

def main():
    # 获取用户输入的好友全称和消息内容
    people = input("请输入好友全称: ")
    message = input("请输入要发送的消息: ")
    send_msg(people, message)

if __name__ == "__main__":
    main()