# 线程池：一次性开辟一些线程。我们用户直接给线程池子提交任务。线程任务的调度交给线程池来完成
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor


def fun(name):
    for number in range(1000):
        print(name, number)


if __name__ == "__main__":
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1000):
            t.submit(fun, name=f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("123")
