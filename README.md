# What is this?

This is a pet-project for [this](https://github.com/YakovSava/bot_for_alone_people)

But in fact, this is a small and *easy* project in order to receive compliments even without constant requests to third-party APIs. Perhaps this project will help someone?

## Locale: **ru_RU.UTF-8**

## Examples of using this small API
Here are examples of using this api in your projects. I will be glad if someone really uses this =)
Synchronous request:
```Python
from compliments_getter import get_compliment

def main():
	print("Your compliment: ", get_compliment())

if __name__ == '__main__':
	main()
```
Asynchronous request:
```Python
import asyncio

from asyncio import new_event_loop, get_event_loop
from compliments_getter import get_compliemnt_async

async def other_task():
	for _ in range(10**100):
		pass
	return ...

async def task_for_get_compliement(loop):
	compliment = await get_compliemnt_async(loop=loop)
	return ...

if __name__ == '__main__':
	main_loop = get_event_loop()

	main_loop.run_until_complete(
		asyncio.wait([
			other_task(),
			other_task(),
			other_task(),
			task_for_get_compliement(new_event_loop())
		])
	)
```