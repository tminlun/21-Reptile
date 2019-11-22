# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/23 0023 20:48'


import threading


'''
多线程在同个进程中，所以进程中的全局变量是共享的。
造成一个问题：
    因为线程顺序是无序的，会造成数据错误
    
注：
    1、锁只用在“修改”全局变量值的地方
    2、“访问”全局变量值，不能用锁
'''

VALUE = 0

# 加锁类
Glock = threading.Lock()


# 修改全局变量值
def add_value():
    global VALUE
    # 下个线程进来后先上锁。
    # 等上个线程执行完成（解锁）再执行下个线程，以此类推

    Glock.acquire()  # 上锁
    for x in range(1000000):
        # 修改全局变量
        VALUE += 1
    Glock.release()  # 解锁



    print("Value为： %s" % VALUE)
    # 期待：第一次为：10000；第二次为：20000
    # 输出第一次为：1275195；第二次为：1300694


def main():
    for i in range(2):
        # 执行两次
        '''
        在线程少的时候，会执行“两”次t1
        但在线程多的时候，会“同时”执行t1
        '''
        t1 = threading.Thread(target=add_value)
        t1.start()



if __name__ == '__main__':
    main()

