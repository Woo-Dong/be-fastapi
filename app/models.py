
from datetime import datetime 
from enum import Enum 
from typing import List 

from pydantic import Field 
from pydantic.main import BaseModel 
from pydantic.networks import EmailStr, IPvAnyAddress 

class UserRegister(BaseModel): 
    email: str = None 
    pw: str = None 

class SnsType(str, Enum): 
    email: str = "email" 
    facebook: str = "facebook"
    google: str = "google" 
    kakao: str = "kakao" 

class Token(BaseModel): 
    Authorization: str = None 


class UserToken(BaseModel): 
    id: int 
    email: str = None 
    name: str = None 
    phone_number: str = None 
    profile_img: str = None 
    sns_type: str = None 

    class Config: 
        orm_mode = True 

'''
class UserMe(BaseModel):
    id: int
    email: str = None
    name: str = None
    phone_number: str = None
    profile_img: str = None
    sns_type: str = None

    class Config:
        orm_mode = True
'''