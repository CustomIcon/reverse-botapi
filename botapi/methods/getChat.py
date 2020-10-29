from botapi import app, sessions
from pyrogram import errors
import json 


@app.get('/getChat')
@app.post('/getChat')
async def get_chat(token: str, chat_id: int):
    try:
        client = await sessions(token)
    except errors.AccessTokenInvalid:
        return {
            "error": 'The bot access token is invalid (caused by "ImportBotAuthorization")'
        }
    except errors.AccessTokenExpired:
        return {
            "errors": 'The bot token is invalid (caused by "auth.ImportBotAuthorization")'
        }
    try:
        c = await client.get_chat(chat_id)
    except errors.PeerIdInvalid:
        return {
            "error": "The id/access_hash combination is invalid"
        }
    return json.loads(str(c))
