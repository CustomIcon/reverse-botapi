from typing import Union
from botapi import app, sessions
import json


@app.get('/getUser')
@app.post('/getUser')
async def get_user(token: str, user_id: Union[int, str]):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        u = await client.get_users(user_id)
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(u))
