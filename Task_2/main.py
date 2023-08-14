from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime as dt
import gspread
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

googlesheet_id = os.getenv('GT')
gc = gspread.service_account(filename='/Users/ekks-job/Downloads/botsuptech-d5124d5ef648.json')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ буду записывать в гугл док все что ты мне напишешь")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        dd = message.text
        nm = message.from_user
        d = dict(nm)
        user = d['username']
        srt = {}
        current_time = dt.now().isoformat()
        srt.update({'text': dd, 'login': user, 'dt': current_time})
        await message.answer("Сообщение записано")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([dd, user, current_time])
    except Exception as e:
        current_time = dt.now().isoformat()
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([str(e), current_time])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

