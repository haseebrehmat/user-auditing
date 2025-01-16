"""
Pydantic schemas for data validation and serialization.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)



class UserAuditResponse(BaseModel):
    id: int
    user_id: int
    operation: str
    timestamp: datetime  # Use datetime here and format it explicitly in the response
    previous_data: dict | None
    new_data: dict | None

    model_config = ConfigDict(from_attributes=True)


    @staticmethod
    def format_timestamp(value: datetime) -> str:
        return value.isoformat()

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: dict):
        if "timestamp" in value and isinstance(value["timestamp"], datetime):
            value["timestamp"] = cls.format_timestamp(value["timestamp"])
        return value
