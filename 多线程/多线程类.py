# 多线程 法2
from threading import Thread

class MyThread(Thread):
    def run(self): # 固定的，线程可以执行之后，被执行的就是 run()
        for i in range(100):
            print(f'子线程1：{i}')




if __name__ == '__main__':

    t = MyThread()
    # t.run() #方法的调用 
    t.start()
    for i in range(100):
        print(f'主线程：{i}')