# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/8 0008 15:36'


import threading, random, time


gMoney = 1000
gLock = threading.Lock()  # 锁对象

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
            gLock.acquire()  # 加锁，防止其他线程插队
            if gTimes >= gTotalTimes:
                # 次数大于10， 解锁和退出循环
                gLock.release()
                break
            gMoney += money
            print("%s生产了%d元钱，剩余%s元钱" % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gLock.release()  # 生产完，释放锁
            time.sleep(0.5)


# 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)

            gLock.acquire()  # 加锁，防止其他线程插队
            if gMoney >= money:
                # 足够钱消费
                gMoney -= money
                print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money,gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
            print("%s消费了%d元钱，剩余%d元钱，不足！" % (threading.current_thread(), money, gMoney))

            gLock.release()  # 释放锁
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
