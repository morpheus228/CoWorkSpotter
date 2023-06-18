from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.misc import replicas

start_router = Router()


@start_router.message(Command("start"))
async def start_bot(message: Message, state: FSMContext):
    await message.answer(replicas.start.substitute())
