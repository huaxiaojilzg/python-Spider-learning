# 多线程
# def func():
#     for i in range(100):
#         print(f'func:{i}')


# if __name__ == '__main__':
#     func()
#     for i in range(100):
#         print(f'func:{i}')

# 多线程 法1
from threading import Thread # 线程类

def func1():
    for i in range(100):
        print(f'func1:{i}')
def func2():
    for i in range(100):
        print(f'func2:{i}')

if __name__ == '__main__':
    t1 = Thread(target=func1) # 产生一个新的线程
    t1.start() # 多线程状态为可以开始，具体时间由cpu决定
    t2 = Thread(target=func2)
    t2.start()
    for i in range(100):
        print(f'main:{i}')