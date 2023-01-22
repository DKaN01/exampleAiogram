from aiogram import Bot, Dispatcher, executor, types

from database import addMessage
from _token import getToken


bot = Bot(getToken())
dp = Dispatcher(bot)


@dp.message_handler()
async def on_message( msg: types.Message ):
    addMessage(msg)
    await msg.answer(msg.text)


def main() -> None:
    executor.start_polling(dp)


if __name__ == "__main__":
    main()