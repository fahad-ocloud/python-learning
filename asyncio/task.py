import asyncio

async def fetch_data(delay,id):
    print("Fetching data....")
    await asyncio.sleep(delay)
    print(f"Data fetched : {id}")
    return {"data":"Some Data"} 

async def foo():
    try:
        task1 = asyncio.create_task(fetch_data(2,1))
        task2 = asyncio.create_task(fetch_data(6,2))
        task3 = asyncio.create_task(fetch_data(3,3))
        result1 = await task1
        result2 = await task2
        result3 = await task3
        print(f"hello world this is asyncio 1: {result1}")
        print(f"hello world this is asyncio 2: {result2}")
        print(f"hello world this is asyncio 3: {result3}")
    except:
        print("error occurr")

def main():
    inp = int(input("Enter 1 to create an event loop"))
    if inp == 1:
        asyncio.run(foo())
    else:
        fetch_data(1,1)
        fetch_data(2,2)
        fetch_data(2,2)

   
main()