# 1 call_soon

import asyncio

def callback(sleep_time):
    print("sleep {}s".format(sleep_time))

def stoploop(loop):
    loop.stop()

if __name__ =="__main__":
    loop = asyncio.get_event_loop()
    loop.call_soon(callback,2)
    loop.call_soon(stoploop,loop)
    loop.run_forever()