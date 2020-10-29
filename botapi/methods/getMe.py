from botapi import app, sessions

@app.get('/getMe')
@app.post('/getMe')
async def get_me(token: str):
    client = await sessions(token)
    me = await client.get_me()
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