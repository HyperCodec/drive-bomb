from threading import Thread
import asyncio, os

# config (if someone wants to run this for some reason)
output_dir = "foo.txt"
async_tasks = 200

# the fun part
async def adder():
    global data
    
    while True:
        data += "𒁃"
    
def save():
    while True:
        with open(output_dir, "a") as f:
             f.write(data)

        os.system('clear')
        print(f'filesize (bytes): {os.path.getsize(output_dir)}')
            
data = ""
t = Thread(target=save)
t.start()
    
for i in range(async_tasks):
    asyncio.run(adder())
