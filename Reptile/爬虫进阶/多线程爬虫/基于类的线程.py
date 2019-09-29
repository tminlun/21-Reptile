# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/23 0023 20:03'


'''
基于类的线程：
    1、需要执行的线程，必须放在run方法中
    2、可以在类中定义其他方法和属性
'''

import threading
import time


class CodeingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("我在写代码 %s。当前线程名：%s" % (x, threading.current_thread()))
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("我在画画 %s。当前线程名：%s" % (x, threading.current_thread()))
            time.sleep(1)


def main():
    # 创建类，即创建线程
    t1 = CodeingThread()
    t2 = DrawingThread()

    # 执行多线程（方法同时执行）
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
