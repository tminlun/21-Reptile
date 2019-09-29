# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/23 0023 19:27'

import threading  # 线程
import time

'''
线程和进程：
    1、多线程：同步实现多个功能。
    2、进程：后台运行即进程
    
    两者关系：
        1、进程：火车，线程：火车的每一节车厢。
        2、车厢离开火车是无法跑动的
        3、火车有多个车厢。多线程是为了提高效率
'''



# # 传统方法（先代码，在画画）
# count = 0
# def codeing():
#     global count
#     for x in range(3):
#         # print("我在写代码 %s" % x)
#         count += 1
#         time.sleep(1)
#
#
# def drawing():
#     global count
#     for x in range(3):
#         # print("我在画画 %s" % x)
#         count += 1
#         time.sleep(1)
#
#
# def main():
#     codeing()
#     drawing()
#     print(count)  # 6 执行了6次
#
#
# if __name__ == '__main__':
#     main()


# 多线程（同时写代码和画画）
count = 0


def codeing():
    global count
    for x in range(3):
        # print("我在写代码 %s。当前线程名：%s" % (x, threading.current_thread()))
        count += 1
        time.sleep(1)


def drawing():
    global count
    for x in range(3):
        # print("我在画画 %s。当前线程名：%s" % (x, threading.current_thread()))
        count += 1
        time.sleep(1)


def main():
    global count
    # 创建线程类
    t1 = threading.Thread(target=codeing)
    t2 = threading.Thread(target=drawing)

    # 执行多线程
    t1.start()
    t2.start()
    print(count)  # 2： 只执行了两次

    # 查看线程数（main()、t1、t2），一个进程有几个线程
    # print(threading.enumerate())


if __name__ == '__main__':
    main()

