from botapi import app, sessions
from pyrogram import errors

@app.get('/getMe')
@app.post('/getMe')
async def get_me(token: str):
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
    me = await client.get_me()
    try:
        return {
            "id": me.id,
            "is_self": me.is_self,
            "is_contact": me.is_contact,
            "is_mutual_contact": me.is_mutual_contact,
            "is_deleted": me.is_deleted,
            "is_bot": me.is_bot,
            "is_verified": me.is_verified,
            "is_restricted": me.is_restricted,
            "is_scam": me.is_scam,
            "is_support": me.is_support,
            "first_name": me.first_name,
            "username": me.username,
            "photo": {
                "small_file_id": me.photo.small_file_id,
                "big_file_id": me.photo.big_file_id
            }
        }
    except AttributeError:
        return {
            "id": me.id,
            "is_self": me.is_self,
            "is_contact": me.is_contact,
            "is_mutual_contact": me.is_mutual_contact,
            "is_deleted": me.is_deleted,
            "is_bot": me.is_bot,
            "is_verified": me.is_verified,
            "is_restricted": me.is_restricted,
            "is_scam": me.is_scam,
            "is_support": me.is_support,
            "first_name": me.first_name,
            "username": me.username
        }