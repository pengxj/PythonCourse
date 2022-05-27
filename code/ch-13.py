import threading
import time

#===============直接用Thread创建线程
def func1(x, y):
    for i in range(x, y):
        print(i)
    time.sleep(5)
t1 = threading.Thread(target=func1, args=(10, 30))
t1.start()
t1.join(5)         #注释掉这里试试
t2 = threading.Thread(target=func1, args=(50, 60))
t2.start()
# t2.join(5)          #注释掉这里试试
print(t1.is_alive())
print(t2.is_alive())

#==========继承Thread
# class myThread(threading.Thread):
#     def __init__(self, num, threadname):
#         threading.Thread.__init__(self, name=threadname)
#         self.num = num
#     def run(self):
#         time.sleep(self.num)         #阻塞线程self.num秒
#         print(self.num)
#
# t1 = myThread(1, 't1')
# t2 = myThread(5, 't2')
# # t2.daemon = True #守护线程，直接退出。注销试试
# print(t1.daemon)
# print(t2.daemon)
#
# t1.start()
# t2.start()

##=========Lock线程同步
# class myThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         global x                    #声明全局变量
#         # lock.acquire()              #获取锁，进入临界区
#         for i in range(3):
#             x = x + i
#         time.sleep(1)
#         print(x)
#         # lock.release()              #释放锁，退出临界区
#
# # lock = threading.Lock()      #创建锁，这里也可以使用RLock
# tl = []
# for i in range(10):          #创建10个线程
#     t = myThread()
#     tl.append(t)
# x = 0
# for i in tl:                 #启动10个线程
#     i.start()
#     i.join()

##==========condition实现同步：生产者消费者模型
# import random
# class Producer(threading.Thread):
#     def __init__(self, threadname):
#         threading.Thread.__init__(self,name=threadname)
#     def run(self):
#         while True:
#             global x
#             time.sleep(random.randrange(1, 5))
#             con.acquire()
#             if x == 20:
#                 print('Producer waiting....')
#                 con.wait()
#                 print('Producer resumed')
#             print('Producer:', end=' ')
#             for i in range(20):
#                 print(x, end=' ')
#                 x = x + 1
#             print(x)
#             con.notify_all()
#             con.release()
# class Consumer(threading.Thread):
#     def __init__(self, threadname):
#         threading.Thread.__init__(self, name=threadname)
#     def run(self):
#         while True:
#             global x
#             time.sleep(random.randrange(1, 5))
#             con.acquire()
#             if x == 0:
#                 print('Consumer waiting....')
#                 con.wait()
#                 print('Consumer resumed')
#             print('Consumer:', end=' ')
#             for i in range(20):
#                 print (x, end=' ')
#                 x = x - 1
#             print(x)
#             con.notify_all()
#             con.release()
#
# con = threading.Condition()
# x = 0
# p = Producer('Producer')
# c = Consumer('Consumer')
# c.start()
# p.start()
# # 等待两个线程都运行结束
# time.sleep(5)
# print('\nAfter Producer and Consumer all done:',x)

##==========quence对象 消费者生产者
# import queue
# class Producer(threading.Thread):
#     def __init__(self, threadname):
#         threading.Thread.__init__(self, name=threadname)
#
#     def run(self):
#         for i in range(10):
#             myqueue.put(i)
#             print(self.getName(), ' put ', i, ' to queue.')
#
#
# class Consumer(threading.Thread):
#     def __init__(self, threadname):
#         threading.Thread.__init__(self, name=threadname)
#
#     def run(self):
#         for i in range(10):
#             print(self.getName(), ' get ', myqueue.get(), ' from queue.')
#
# myqueue = queue.Queue()
# Consumer('Consumer').start()
# time.sleep(2)
# Producer('Producer').start()


# from multiprocessing import Process
# import os
#
# def f(name):
#     print('module name:', __name__)
#     print('parent process:', os.getppid())   #查看父进程ID
#     print('process id:', os.getpid())        #查看当前进程ID
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))     #创建进程
#     p.start()                                #启动进程
#     p.join()                                 #等待进程结束


# from multiprocessing import Pool
# from statistics import mean
# import time
# if __name__ == '__main__':
#     x = [list(range(10)), list(range(20,30)),
#          list(range(50,60)), list(range(80,90)),list(range(10)), list(range(20,30)),
#          list(range(50,60)), list(range(80,90)),list(range(10)), list(range(20,30)),
#          list(range(50,60)), list(range(80,90))]
#     s = time.time()
#     with Pool(2) as p:
#         print(p.map(mean, x))
#         print(p.map(sum, x))
#
#     print(f'time used {time.time()-s}')
