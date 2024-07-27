# https://www.youtube.com/watch?v=6EBBWv6tuA8
# https://www.youtube.com/watch?v=9g5IZDkwAC0

# https://www.youtube.com/watch?v=olYdb0DdGtM&t=47s


# concurrency dealing with multiple tasks at once
# paralleism -> use more cpu or compute to make computation faster -> add more workers , cores
# concurrency - > permit multiple tasks to proceed without waiting for each other.
# parell running of thread is not allowed
# I/o bound task - Thread >>>> use Thread which share data with minimal cpu uses
# GIL
# multiple things happen at the same time - parrellism


# asyncio -> best for task which wait a lot like n/w request and reading a files -? I/O operations
# [https://www.youtube.com/watch?v=Qb9s3UiMSTA&t=386s]
# event loop, coroutine, await , tasks, gather, TaskGroup, asyncr context managers, future, synchronization of coroutine[LOCK, semaphores, event], Queue

# function in asyncio are called coroutine, Coroutine object

# asyncio is a perfect fit for IO bound, web server, Networking, data streaming, GUI Apps, network requests or file I/O

# asynxio.gather use exception handling
# https://fionamuthoni18.medium.com/asyncio-a-practical-guide-to-seven-essential-functions-647a0b9ff9ae


# data ingestion data loading web scrapping task used by data engineer
# https://www.arecadata.com/i-have-to-execute-a-function-in-parallel/

#inside module there can be functions and class, Variable
import multiprocessing  # its a module
import threading
import asyncio

from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool
from multiprocessing import Manager, Process
from aiohttp import ClientSession, ClientError
import numpy
import pandas
import signal
from collections import (
    defaultdict,
    OrderedDict,
    deque,
    UserDict,
    UserList,
    UserString,
    Counter,
)

print("Hello Asyncio......")


async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


# main() [Coroutine Object][it needed to be waited to get the results]

asyncio.run(main())  # [waited handled by asyncio]

# [gather pass all the coroutine return as a list]

# import asyncio
# import threading
# from random import randint

# import aiohttp  # type: ignore
# import aiofiles  # type: ignore
# import aiomultiprocess

# NUM_CONSUMERS = 8


# async def producer(queue: asyncio.Queue) -> None:
#     while True:
#         random_isbn = "".join(["{}".format(randint(0, 9)) for _ in range(0, 10)])
#         queue.put_nowait(random_isbn)
#         await asyncio.sleep(0.05)


# async def consumer(consumer_idx: int, queue: asyncio.Queue) -> None:
#     while True:
#         isbn = await queue.get()
#         async with aiohttp.ClientSession() as session:
#             async with session.get(
#                 "https://openlibrary.org/api/books?bibkeys=ISBN:"
#                 + isbn
#                 + "&format=json"
#             ) as resp:
#                 book_descriptor = await resp.json()
#                 if book_descriptor != {}:
#                     print(
#                         f"Consumer {consumer_idx} found valid ISBN. Current queue size: {queue.qsize()}. Discovered book: {book_descriptor}"
#                     )
#         queue.task_done()


# async def main():
#     queue = asyncio.Queue()
#     await asyncio.gather(*([producer(queue)] + [consumer(idx, queue) for idx in range(NUM_CONSUMERS)])
#     )


# if __name__ == "__main__":
#     asyncio.run(main())
# ---------------------------------------------######-------------------------------------------------

# import asyncio
# import random

# import aiomultiprocess


# async def coro_func(value: int) -> int:
#     await asyncio.sleep(random.randint(1, 3))
#     return value * 2


# async def main1():
#     results = []
#     async with aiomultiprocess.Pool() as pool:
#         async for result in pool.map(coro_func, [1, 2, 3]):
#             results.append(result)

#         # The result depends on the order in which the parameters are passed in,
#         # not on which task end first
#         # Output: [2, 4, 6]
#         print(results)


# if __name__ == "__main__":
#     asyncio.run(main1())
