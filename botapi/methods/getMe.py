from botapi import app, sessions
import json

@app.get('/getMe')
@app.post('/getMe')
async def get_me(token: str):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    me = await client.get_me()
    return json.loads(str(me))