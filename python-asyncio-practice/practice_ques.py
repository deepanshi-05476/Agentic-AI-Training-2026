1. import asyncio

async def foo():
    print("A")
    await asyncio.sleep(0)
    print("B")

async def main():
    task = asyncio.create_task(foo())
    print("C")
    await task
    print("D")

asyncio.run(main())
      
Output
C
A
B
D
      
Explanation
create_task(foo()) schedules foo() to run.
Control remains in main().
print("C") executes.
await task gives control to foo().
foo() prints A.
await asyncio.sleep(0) yields control back to the event loop.
foo() resumes and prints B.
Task finishes.
main() continues and prints D.

2. import asyncio

async def worker():
    print("worker start")
    await asyncio.sleep(1)
    print("worker end")

async def main():
    task = asyncio.create_task(worker())
    print("main running")
    await task

asyncio.run(main())
      
Output
main running
worker start
(worker waits 1 second)
worker end
Explanation
      
worker() is scheduled.
main() immediately prints "main running".
await task waits for worker.
Worker starts and prints "worker start".
Sleeps for 1 second.
Prints "worker end".
      
3. import asyncio

async def job(delay):
    await asyncio.sleep(delay)

async def main():
    await asyncio.gather(
        job(3),
        job(2),
        job(1)
    )

asyncio.run(main())
Output
(no output)
Total Time

≈ 3 seconds

Explanation

gather() runs all coroutines concurrently.

Timeline:

0s -> start all jobs
1s -> job(1) finishes
2s -> job(2) finishes
3s -> job(3) finishes

Main waits until all finish.

Total time = longest delay = 3 seconds

4. import asyncio

async def job(delay):
    await asyncio.sleep(delay)

async def main():
    await job(3)
    await job(2)
    await job(1)

asyncio.run(main())
      
Output
(no output)
Total Time

≈ 6 seconds

Explanation
These execute sequentially:

job(3) -> 3s
job(2) -> 2s
job(1) -> 1s

Total:

3 + 2 + 1 = 6 seconds

Unlike gather(), there is no concurrency.
