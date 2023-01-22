from models import Messages
from aiogram import types


def addMessage(msg: types.Message) -> None:
    message = Messages(user_id=msg.from_user.id, text=msg.text, user_full=msg.from_user.full_name, date=msg.date)
    message.save()
    print(f"[{msg.date}]Добавлено сообщение от {msg.from_user.full_name}:{msg.text}")