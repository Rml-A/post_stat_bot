import logging
import os
from aiogram import Bot, Dispather, types
from aiogram.utils import executor
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ADMIN_ID = int(os.getenv("ADMIN_ID"))
CHANNEL = int(os.getenv("CHANNEL"))

@dp.message_handler()
async def handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        match, bet, coef = message.text.split(";")

        post = f"""
🔥 Прогноз
    
⚽ {match}
📊 Ставка: {bet}
💰 Коэф: {coef}
    
#ставка
    """

        await bot.send_message(chat_id=CHANNEL, text=post)
        await message.reply("✅ Опубликовано")

    except Exception as e:
        await message.reply(f"Ошибка: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)