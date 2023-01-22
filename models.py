from peewee import SqliteDatabase, CharField, TextField, PrimaryKeyField, Model
import os


db = SqliteDatabase("db.db")


class Base(Model):
    class Meta:
        database = db 


class Messages(Base):
    id = PrimaryKeyField()
    user_id = CharField()
    text = TextField()
    user_full = CharField()
    date = CharField()


if not os.path.exists("db.db"):
    Messages.create_table()