import asyncio
import time


async def task_schedular(id,task_time):
    # print(f"time : {time}")
    print(f"Execution of task{id} started")
    start = time.time()
    await asyncio.sleep(task_time)
    end = time.time()
    print(f"task {id} executed in {end-start}")

async def main():
    tasks = []
    x=1
    num =  int(input("Enter number of task you want to execute ? "))
    while x<=num:
        task_time = int(input(f"Enter delay time for task {x} : "))
        tasks.append((x,task_time))
        x+=1
    results = await asyncio.gather(*(task_schedular(id,time) for id,time in tasks))

    
asyncio.run(main())