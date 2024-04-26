from aiogram import Bot, Dispatcher, types
import config

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd_handler(message: types.Message):
    await message.reply("Привет! Я бот, который может проверить, может ли человек пройти на аттракцион. Напиши мне возраст и рост в формате: 'возраст рост'")

@dp.message_handler()
async def check_attraction(message: types.Message):
    age, height = map(int, message.text.split())
    if age >= 14 and height >= 140:
        await message.reply("Да, вы можете пройти на аттракцион!")
    else:
        await message.reply("К сожалению, вы не можете пройти на аттракцион.")
