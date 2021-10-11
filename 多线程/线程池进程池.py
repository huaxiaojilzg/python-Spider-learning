# http://xinfadi.com.cn/marketanalysis/0/list/14869.shtml
# 线程池：一次性开辟一些线程，我们用户直接给线程池子提交任务，线程任务的调度
# 例如50个池子，10000个任务

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    # 创建50个线程的线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(10):
            t.submit(fn,name=f'线程{i}')
    # 等待线程池中的任务全都执行完毕，才继续执行--守护进程
    print('123')
