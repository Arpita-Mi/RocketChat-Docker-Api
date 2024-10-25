from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class UserCreate(BaseModel):
    username : str
    password : str
    email : str


class UserLogin(BaseModel):
    username :  str
    password : str



class RoomCreate(BaseModel):
    name: str
    type: str = "c"  

class MessageSend(BaseModel):
    channel: str
    text: str