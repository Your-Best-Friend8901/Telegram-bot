from aiogram import Bot,Dispatcher
import asyncio
from BotToken import TOKEN
from Router import message_handler
from aiogram.fsm.storage.memory import MemoryStorage
from Routercall_back import call_back

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(message_handler)
dp.include_router(call_back)

async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())
