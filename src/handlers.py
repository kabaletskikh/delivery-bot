from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import config


# ------ CONSTS ------
cfg = config.Config()
bot = Bot(token = cfg.get("handler", "token"))

dp = Dispatcher (
    bot,
    storage = MemoryStorage()
)



# ------ HANDLERS ------
# /commands ------
@dp.message_handler(state="*", commands=['start'])
async def process_start_command(message: types.Message):
    print("start command")


# text & keyboard commands ------
@dp.message_handler(state="*", text='тест')
async def process_start_command(message: types.Message):
    print("тест")


# inline commands ------
@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    print("inline button pressed")



# ------ SAFE LAUNCH ------
async def shutdown(dispatcher: Dispatcher):
    print("Shutting down the bot!")


if __name__ == '__main__':
    print("Запускаем молодого!")
    executor.start_polling(dp, on_shutdown=shutdown)