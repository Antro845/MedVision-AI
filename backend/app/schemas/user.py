from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    fullname: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    fullname: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        from_attributes = True