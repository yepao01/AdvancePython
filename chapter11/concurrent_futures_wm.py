from concurrent.futures import ThreadPoolExecutor,as_completed,wait
import time

def get_html(times):
    time.sleep(times)
    print("got page {}s success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# task1 = executor.submit(get_html,(2))
# task2 = executor.submit(get_html,(3))

#获取已经成功的task的返回  推荐使用
urls = [3,2,4]# 模拟
all_task = [executor.submit(get_html,(url)) for url in urls]
# wait(all_task)

for future in as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

# 通过executor的map获取已完成的task
# for data in executor.map(get_html,urls):
#     print("get {} page success".format(data))

# #done 用于判定任务是否完成
# print(task1.done())
# print(task2.cancel())
# time.sleep(4)
# print(task1.done())
#
# #result 可以获取task的执行结果
# print(task1.result())

