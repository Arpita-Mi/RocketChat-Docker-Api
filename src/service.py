from fastapi import HTTPException
import httpx
from .config import settings


ROCKET_CHAT_URL = settings.Base_Url
tokens  = {}

async def login_user(username : str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ROCKET_CHAT_URL}/login",
            json={"username": username, "password": password},
            headers={"content": "application/json"},
        )
        if response.status_code == 200:
            data = response.json()
            auth_token = data["data"]['authToken']
            user_id = data["data"]["userId"]
            tokens["auth_token"] = auth_token
            tokens["user_id"] = user_id
            return data
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())


async def send_message(channel = str , text =str):
    auth_token = tokens['auth_token']
    user_id = tokens['user_id']
    if 'user_id' not in tokens or 'auth_tokens' not in tokens:
        raise HTTPException("User not authenticated")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{ROCKET_CHAT_URL}/chat.postMessage',
            json={"channel": channel, "text": text},
            headers={
                'Content-Type': 'application/json',
                'X-Auth-Token': auth_token,
                'X-User-Id': user_id
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())