from os.path import exists
from asyncio import AbstractEventLoop, get_event_loop
from json import loads
from aiofiles import open as aiopen
from downoloader import Load

load = Load()

if not exists('compliments.json'):
    with open('compliments.json', 'w', encoding='utf-8') as file:
        file.write('''{
    "complients": []
}''')
    raise ValueError('Please fill file "compliments.json"')

def get_compliment() -> str:
    with open('compliments.json', 'r', encoding='utf-8') as file:
        compliemnts = loads(file.read())['compliments']
    return load.choice(compliemnts)

async def get_compliemnt_async(loop:AbstractEventLoop=get_event_loop()) -> str:
    async with aiopen('compliments.json', 'r', encoding='utf-8', loop=loop) as file:
        compliments = await loop.run_in_executor(None, loads, await file.read())
    return await loop.run_in_executor(None, load.choice, compliments)