from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


# Properties to receive via API on update
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


# Properties to return via API
class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
