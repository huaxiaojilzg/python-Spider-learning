from multiprocessing import Process
from threading import Thread

# def func():
#     for i in range(1000):
#         print(f'子进程:{i}')


# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()

#     for i in range(1000):
#         print(f'主进程:{i}')

def func(name):
    for i in range(1000):
        print(f'{name}:{i}')


if __name__ == '__main__':
    t1 = Thread(target=func,args=['哈哈'])
    t1.start()

    t2 = Thread(target=func,args=['嘤嘤嘤'])
    t2.start()
