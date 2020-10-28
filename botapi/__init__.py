from fastapi import FastAPI
from os import environ
from configparser import ConfigParser
from pyrogram import Client

PORT = environ.get('PORT', None)

app = FastAPI()

config = ConfigParser()
config.read("botapi.ini")

async def sessions(token):
    client = Client(
        ':memory:',
        api_id=int(config.get('pyrogram', 'api_id')),
        api_hash=config.get('pyrogram', 'api_hash'),
        bot_token=token
    )
    await client.start()
    return client