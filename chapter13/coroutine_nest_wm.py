# # 1 run_unit_complete
# import asyncio
# loop = asyncio.get_event_loop()
# #一直运行
# loop.run_forever()
# #运行完某个协程自动停止
# loop.run_until_complete(tasks)

# 1. loop会被放到future里
# 2. 取消future(task)

# # 2. 协程的取消
import asyncio
import time

async def get_html(sleep_time):
    print("waiting")
    await asyncio.sleep(sleep_time)
    print("done after {}s".format(sleep_time))

if __name__ == "__main__":
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)
    tasks = [task1,task2,task3 ]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

# # 3.协程的嵌套










