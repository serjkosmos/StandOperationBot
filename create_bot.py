from aiogram import Bot
from aiogram.dispatcher import Dispatcher
# import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5283752617:AAFObfX9VCrJ_exbVOwr62PSEWe4b2XitlA'
storage=MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

