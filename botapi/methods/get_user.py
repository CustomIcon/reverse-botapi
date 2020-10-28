from botapi import app, sessions
from pyrogram.errors import PeerIdInvalid

@app.post('/getUser')
async def get_user(token: str, user_id: int
    ):
    client = await sessions(token)
    try:
        me = await client.get_users(user_ids=user_id)
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
            "last_name": me.last_name,
            "username": me.username,
            "status": me.status,
            "language_code": me.language_code,
            "dc_id": me.dc_id,
            "photo": {
                "small_file_id": me.photo.small_file_id,
                "big_file_id": me.photo.big_file_id
            }
        }
    except PeerIdInvalid:
        return {
            "error": "The id/access_hash combination is invalid"
        }