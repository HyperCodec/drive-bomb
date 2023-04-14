import asyncio
from multiprocessing import Pool, Value
from ctypes import c_char_p

# config (if someone wants to run this for some reason)
output_dir = "foo.txt"
processes = 100

# the fun part
data = Value(c_char_p, 0)

def add():
    global data

    with data.get_lock():
        data.value = c_char_p(data.value + "𒁃")

if __name__ == "__main__":
    async def save():
        while True:
            with open(output_dir, "a") as f:
                f.write(data)

    print("making big data")
    with Pool(processes) as p:
        p.map(add, range(10000000))
  
    print("making big file with data")

    asyncio.run(save())
