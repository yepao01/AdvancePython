import asyncio
import time
from requests import get
from functools import partial


# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2) #time.sleep(2) 是同步操作
#     print("end get url")
# #事件循环
# if __name__ == "__main__":
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("https://www.cnblogs.com/aademeng/articles/7241485.html") for i in range(100)]
#     # loop.run_until_complete(get_html("https://www.cnblogs.com/aademeng/articles/7241485.html"))
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time()-start)
#----------------------------------------------------------------------------


# 获取协程的返回值 添加callback
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)  # time.sleep(2) 是同步操作
#     return "bobby"
#
# def callback(url, future):
#     print(url)
#     print("send email to bobby")
#
# if __name__ == "__main__":
#     start = time.time()
#     # 获取EventLoop  事件循环
#     loop = asyncio.get_event_loop()
#     # 获得future对象 在内部注册到loop中（看源码）  把协程包装成task，返回task
#     get_future = asyncio.ensure_future(get_html("https://www.cnblogs.com"))
#     # 协程执行结束后 执行callback  partial为了callback时添加其他参数
#     get_future.add_done_callback(partial(callback,"https://www.cnblogs.com")) #偏函数
#     # 执行 协程
#     loop.run_until_complete(get_future) #可以接受协程 future task 3种
#     # 获取协程的返回值
#     print(get_future.result())
#     print(time.time() - start)
#
#     # start = time.time()
#     # loop = asyncio.get_event_loop()
#     # # 协程注册在loop中
#     # task = loop.create_task(get_html("https://www.cnblogs.com"))
#     # task.add_done_callback(callback)
#     # loop.run_until_complete(task)
#     # print(task.result())
#     # print(time.time() - start)

#----------------------------------------------------------------------------------

#wait gather

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2) #time.sleep(2) 是同步操作
    print("end get url")
#事件循环
if __name__ == "__main__":
    # start = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html("https://www.cnblogs.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.time()-start)

    # start = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html("https://www.cnblogs.com") for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time()-start)

#gather 更加高层
    start = time.time()
    loop = asyncio.get_event_loop()
    group1 = [get_html("https://www.cnblogs.com") for i in range(2)]
    group2 = [get_html("https://www.cnblogs110.com") for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()
    loop.run_until_complete(asyncio.gather(group1,group2))
    print(time.time()-start)









