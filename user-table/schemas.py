from pydantic import BaseModel, validator, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    phonenumber : str

    @validator('phonenumber')
    def validate_phonenumber(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError("Please enter a valid phone number")
        return v

class UserDisplay(BaseModel):
    username: str
    email: str
    phonenumber : str

    class Config():
        orm_mode = True