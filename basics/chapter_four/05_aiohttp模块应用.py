# requests.get() # 同步的代码 ——> 异步操作aiohttp
# pip install  aiohttp

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2021/1021/25721be644008089b08004c82f5e1e23.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/1020/d33d25225ae37bfac2b474b998183b23.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/1020/b618d53145439618a6f1982af394dc01.jpg"
]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]    # 从右边切，切一次，得到[1]位置的内容
    async with aiohttp.ClientSession() as session:  # requests
        async with session.get(url) as resp:    # resp = requests.get()
            # 请求回来了，写入文件
            # 可以自己去学习一个模块，aiofiles
            with open(name, mode='wb') as f:    # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起 resp.text
    print("OK!")

    # s = aiohttp.ClientSession()     # <==> requests
    # 发送请求。
    # 得到图片内容
    # 保存文件
    pass


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)
    pass


if __name__ == "__main__":
    asyncio.run(main())

