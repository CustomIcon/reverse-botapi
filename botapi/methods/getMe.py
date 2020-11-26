from botapi import app, sessions
import json

@app.get('/getMe')
@app.post('/getMe')
async def get_me(token: str):
    client = await sessions(token)
    me = await client.get_me()
    return json.loads(str(me))