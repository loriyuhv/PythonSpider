import asyncio
import time
# 概念
"""
import time


def func():
    print("I love dawn")
    time.sleep(3)   # 让当前的线程处于阻塞状态。CPU是不为我工作的
    print("I really love dawn.")


if __name__ == "__main__":
    func()

# input()   # 程序也是处于阻塞状态
# requests.get() # 在网络请求返回数据之前，程序也是处于阻塞状态的
# 一般情况下，当程序处于IO操作的时候，线程都会处于阻塞状态

# 协程：当程序遇见了IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起执行
# 多任务异步操作

# 上方所讲的一切，都是在单线程的条件下。
"""

# python编写携程的程序

# 协程使用
# 1.
"""
import asyncio


async def func():
    print("Hello world")


if __name__ == "__main__":
    g = func()   # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    # print(g)
    asyncio.run(g)  # 协程程序运行需要asyncio模块的支持
"""

# 2.
"""
import asyncio
import time

async def func1():
    print("Hello world")
    # time.sleep(3)   # 当程序出现同步操作的时候，异步就中断了。
    await asyncio.sleep(3)    # 异步操作的代码
    print("Hello World")


async def func2():
    print("Hello loriyuhv")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("Hello Loriyuhv")


async def func3():
    print("Hello func3")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("Hello Func3")


async def func4():
    print("Hello func4")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("Hello Func4")


if __name__ == "__main__":
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        f1, f2, f3
    ]
    t1 = time.time()
    # 一次性启动多个任务（协程）
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2-t1)    # 前：8.035661458969116 后：3.011827230453491
"""

# 3.
"""

async def func1():
    print("Hello world")
    # time.sleep(3)   # 当程序出现同步操作的时候，异步就中断了。
    await asyncio.sleep(3)    # 异步操作的代码
    print("Hello World")


async def func2():
    print("Hello loriyuhv")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("Hello Loriyuhv")


async def func3():
    print("Hello func3")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("Hello Func3")


async def main():
    # 第一种写法
    '''
    f1 = func1()
    await f1    # 一般await挂起操作放在协程对象前面
    '''
    # 第二种写法
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    # 注意：3.8以及之后的版本不支持
    # 必须包装程task对象 # Coroutines will be wrapped in Tasks.
    tasks = [
        asyncio.create_task(func1()),
        ....
    ]
    
    await asyncio.wait(tasks)
    pass


if __name__ == "__main__":
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)
    pass
"""

# 在爬虫领域的应用


async def dwonload(url):
    print("准备下载")
    await asyncio.sleep(2)    # 网络请求
    print("下载完成")


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    tasks = []
    for url in urls:
        d = dwonload(url)
        tasks.append(d)

    await asyncio.wait(tasks)



if __name__ == "__main__":
    asyncio.run(main())
