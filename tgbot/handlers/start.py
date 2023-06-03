from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from tgbot.misc import replicas, keyboards
from tgbot.misc.funcs import get_nearest_pubs
from tgbot.misc.states import mainSG
from tgbot.models import Pub

start_router = Router()


@start_router.message(Command("start"))
async def start_bot(message: Message, state: FSMContext):
    pass
