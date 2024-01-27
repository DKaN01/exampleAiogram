from aiogram import Bot, Dispatcher, Router, types
import asyncio

from database import addMessage
from _token import getToken


bot = Bot(getToken())
dp = Dispatcher()
router = Router()


@router.message()
async def on_message( msg: types.Message ):
    addMessage(msg)
    await msg.answer(msg.text)


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())