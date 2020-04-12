import time

import requests
import timeit
import asyncio

my_repo_url = 'https://bitbucket.micron.com/bbdc/users/yhkao'
loop = asyncio.get_event_loop()
start_time = time.process_time()


async def send_req(url, id_):
    t = time.process_time()
    print(f"[{id_}]Send a request at", t - start_time, "seconds.")
    res = await loop.run_in_executor(None, lambda: requests.get(url))
    t = time.process_time()
    time.sleep(3)
    print(f"[{id_}]Receive a response at", t - start_time, "seconds.")


tasks = []
for idx in range(5):
    task = loop.create_task(send_req(my_repo_url, idx))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
