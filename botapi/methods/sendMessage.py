from typing import Optional, Union
from botapi import app, sessions
from pyrogram import errors
from pyrogram import types
import json

@app.get('/sendMessage')
@app.post('/sendMessage')
async def sned_message(
    token: str,
    chat_id: Union[int, str],
    text: str,
    parse_mode: Union[str, None] = object,
    disable_web_page_preview: bool = None,
    disable_notification: bool = None,
    reply_to_message_id: int = None,
    schedule_date: int = None,
    reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> "types.Message":
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
        u = await client.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
            schedule_date=schedule_date,
            reply_markup=reply_markup
        )
    except errors.PeerIdInvalid:
        return {
            "error": "The id/access_hash combination is invalid"
        }
    return json.loads(str(u))
