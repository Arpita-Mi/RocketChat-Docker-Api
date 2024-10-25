from fastapi import FastAPI , HTTPException
from .schemas import UserLogin , MessageSend
from .service import login_user , send_message
app = FastAPI()

tokens  = {}

@app.post("/login")
async def login_user_api(user: UserLogin):
    try:
        token = login_user(user.username,user.password)
        return token
    except Exception as e:
        raise HTTPException(status_code= e.status_code, detail={"error" : e})



@app.post("/chat.postMessage")
async def send_message_api(message: MessageSend):
    try:
        response = send_message(message.channel , message.text)
        return response
    except Exception as e:
        raise HTTPException(status_code=response.status_code, detail=response.json())
