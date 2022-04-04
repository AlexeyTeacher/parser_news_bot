from aiogram.types import ParseMode
import aiogram.utils.markdown as fmt
from config import bot_telegram_token
from vc_news_parser import parser
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}!\n "
                         f"Хочешь получить свежую новость с vc.ru?\n"
                         f"Нажми /news")


@dp.message_handler(commands=["news"])
async def news_command(message: types.Message):
    try:
        data = parser()
        if 'Error' in data:
            await message.answer(f"Проблемы с подключением, попробуйте позже")
        data = data[0]
        if data['text']:
            url = data['link_news']
            text = str(data['text']).replace('</p>', '').replace('<p>', '').replace('<br/>', '\n').strip()
            await message.answer(f'<b>{data["title"]}</b>\n\n'
                                 f'{text}\n'
                                 f"{fmt.hide_link(url)}", parse_mode=ParseMode.HTML)
        else:
            await message.answer(f"<b>{data['title']}</b>\n"
                                 f"{fmt.hide_link(data['link_news'])}", parse_mode=ParseMode.HTML)
        data.clear()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    executor.start_polling(dp)
