from fastapi import FastAPI
from os import environ
from configparser import ConfigParser
from pyrogram import Client

PORT = environ.get('PORT', None)
API_ID = environ.get('API_ID', None)
API_HASH = environ.get('API_HASH', None)

app = FastAPI()

config = ConfigParser()
config.read("botapi.ini")

async def sessions(token):
    client = Client(
        ':memory:',
        api_id=int(API_ID or config.get('pyrogram', 'api_id')),
        api_hash=API_HASH or config.get('pyrogram', 'api_hash'),
        bot_token=token
    )
    await client.start()
    return client