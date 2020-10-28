from botapi import app, sessions
from pyrogram.types import User
from pyrogram.errors import PeerIdInvalid

@app.get('/getUser')
@app.post('/getUser')
async def get_user(token: str, user_id: int) -> User:
    client = await sessions(token)
    try:
        return await client.get_users(user_ids=user_id)
    except PeerIdInvalid:
        return {
            "error": "The id/access_hash combination is invalid"
        }