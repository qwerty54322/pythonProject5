from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from parser import get_random_news
TOKEN = '5519372551:AAF08SIrIJqGEOIH6gq1n2-jSoNfrC1rLe4'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['news'])
async def get_news(message: types.Message):
    news = get_random_news()
    await message.answer_photo(photo=news[1],
                               caption=f'*{news[0]}*\n\n'
                                       f'_{news[3]}_\n'
                                       f'{news[4]}\n'
                                       f'[Тык]({news[2]}',
                               parse_mode='Markdown')
if __name__ == '__main__':
    executor.start_polling(dp)