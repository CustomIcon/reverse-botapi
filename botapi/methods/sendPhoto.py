from typing import Optional, Union, BinaryIO
from botapi import app, sessions
from pyrogram import types
import json


@app.post('/sendPhoto')
async def send_photo(
    token: str,
    chat_id: Union[int, str],
    photo: Optional[str] = BinaryIO,
    file_ref: str = None,
    caption: str = "",
    parse_mode: Union[str, None] = object,
    ttl_seconds: int = None,
    disable_notification: bool = None,
    reply_to_message_id: int = None,
    schedule_date: int = None,
    reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
    ) -> "types.Message":
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        u = await client.send_photo(
            chat_id=chat_id,
            photo=photo,
            file_ref=file_ref,
            caption=caption,
            parse_mode=parse_mode,
            ttl_seconds=ttl_seconds,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
            schedule_date=schedule_date,
            reply_markup=reply_markup
        )
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(u))
