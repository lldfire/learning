# import time
# import asyncio


# async def visit_url(url, response_time):
#     """ 访问URL """
#     await asyncio.sleep(response_time)
#     return f'访问{url},得到返回结果'

# start_time = time.perf_counter()
# # task = visit_url('这是个url', 2)
# # asyncio.run(task)


# # # 增加一个任务
# # task2 = visit_url('另外一个url', 3)
# # asyncio.run(task2)

# # async def run_task():
# #     task = visit_url('这是个url', 2)
# #     task2 = visit_url('另外一个url', 3)
# #     await asyncio.run(task)
# #     await asyncio.run(task2)
    
    
# async def run_task():
#     coro = visit_url('这是个url', 2)
#     coro2 = visit_url('另外一个url', 3)
    
#     task = asyncio.creatr_task(coro)
#     task1 = asyncio.creatr_task(coro1)

#     await task
#     await task2
    

# asyncio.run(run_task())

# end_time = time.perf_counter()
# print(f'消耗时间{end_time - start_time}')


# import asyncio

# async def execute(x):
#     print('Number:',x)
#     return x

# coroutine = execute(1)
# print('Coroutine:',coroutine)
# print('After calling execute')

# task=asyncio.ensure_future(coroutine)
# print('Task:',task)

# loop=asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:',task)
# print('After calling loop')


# import asyncio
# import requests

# async def request():
#     url='http://www.baidu.com'
#     status = requests.get(url).status_code
#     return status

# def  callback(task):
#     print('Status:',task.result())

# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print('Task:',task)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:',task)


import asyncio
import requests

async def request():
    url = 'http://www.baidu.com'
    status = requests.get(url).status_code
    return status

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:',tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task Result:',task.result())
