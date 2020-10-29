from botapi import app, sessions
from pyrogram import errors
import json


@app.get('/getUser')
@app.post('/getUser')
async def get_user(token: str, user_id: int):
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
        u = await client.get_users(user_id)
    except errors.PeerIdInvalid:
        return {
            "error": "The id/access_hash combination is invalid"
        }
    return json.loads(str(u))
