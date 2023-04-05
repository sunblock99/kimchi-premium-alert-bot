import telegram
import asyncio
from myToken import *

async def main():
    bot = telegram.Bot(token = token)
    await bot.send_message(chat_id,'테스트!!')

asyncio.run(main()) #봇 실행하는 코드