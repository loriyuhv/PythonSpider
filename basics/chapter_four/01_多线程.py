# 线程：执行单位   进程：资源单位，每一个进程至少要有一个线程


# 单线程
"""
def func():
    for i in range(1000):
        print("func", i)


# 启动每一个程序默认都会有一个主线程
if __name__ == "__main__":
    func()
    for i in range(1000):
        print("main()", i)
"""

# 多线程
# 写法一
"""
from threading import Thread    # 线程类


def func():
    for i in range(1000):
        print("func", i)


if __name__ == "__main__":
    t = Thread(target=func)     # 创建线程并给线程安排任务
    t.start()   # 多线程状态可以开始工作状态，具体的执行时间由CPU决定
    for i in range(1000):
        print("main", i)
"""

# 写法二
"""
from threading import Thread    # 线程类


class MyThread(Thread):
    def run(self):  # 固定的   -> 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("func", i)
        pass


if __name__ == "__main__":
    for i in range(1000):
        t = MyThread()
        # t.run()     # 方法的调用了 ->单线程
        t.start()   # 开启线程
        print("main", i)
    pass
"""

# 给子线程传参
from threading import Thread


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == "__main__":
    t1 = Thread(target=func, args=("李嘉俊",))     # 传参参数必须是元组
    t1.start()

    t2 = Thread(target=func, args=("王师维",))
    t2.start()
    for i in range(1000):
        print("main()", i)

