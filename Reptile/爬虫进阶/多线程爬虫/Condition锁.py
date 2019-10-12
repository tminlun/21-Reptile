# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/8 0008 15:36'


import threading, random, time


gMoney = 1000
gCondition = threading.Condition()  # 锁对象

# 限制次数
gTotalTimes = 10
gTimes = 0


# 生产者
class Produce(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        global gTotalTimes

        while True:
            money = random.randint(100, 1000)

            gCondition.acquire()  # 加锁
            if gTimes >= gTotalTimes:
                # 次数大于10， 解锁和退出循环
                gCondition.release()
                break  # 退出当前循环


            gMoney += money
            # # 生产了钱，就唤醒正在等待的所有线程
            gCondition.notify_all()

            print("%s生产了%d元钱，剩余%s元钱" % (threading.current_thread(), money, gMoney))

            gTimes += 1  # 计算次数
            gCondition.release()  # 释放锁
            time.sleep(0.5)


# 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)

            gCondition.acquire()  # 加锁，防止其他线程插队

            # 每当余额不够，一直等待！进入等待状态，让其他线程先运行。
            while money > gMoney:
                if gTimes >= gTotalTimes:
                    # 超过次数，释放锁
                    gCondition.release()
                    return  # 退出整个函数

                # 当有（其他和当前函数）notify_all后，它将排到其他线程后面，在当前位置继续运行
                gCondition.wait()
                print("%s消费了%d元钱，剩余%d元钱，不足！" % (threading.current_thread(), money, gMoney))

            # 消费完
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money, gMoney))


            gCondition.release()  # 释放锁
            time.sleep(0.5)


def main():
    for x in range(5):
        consumer = Consumer(name="消费者")
        consumer.start()

    for x in range(5):
        produce = Produce(name="生产者")
        produce.start()






if __name__ == '__main__':
    main()
