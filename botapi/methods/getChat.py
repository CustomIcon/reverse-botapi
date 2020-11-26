from typing import Union
from botapi import app, sessions
import json 


@app.get('/getChat')
@app.post('/getChat')
async def get_chat(token: str, chat_id: Union[int, str]):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.get_chat(chat_id)
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(c))
