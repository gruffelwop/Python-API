from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

# User

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserLogin(UserBase):
    pass

# UserResponse

class UserResponseBase(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserResponse(UserResponseBase):
    pass

class UserCreateResponse(UserResponseBase):
    pass

class UserUpdateResponse(UserResponseBase):
    pass

# Post

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class Post(PostBase):
    pass

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

# PostResponse

class PostResponseBase(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    user_id: int
    owner: UserResponseBase
    
    class Config:
        from_attributes = True

class PostResponse(PostResponseBase):
    pass

class PostCreateResponse(PostResponseBase):
    pass

class PostUpdateResponse(PostResponseBase):
    pass

class PostExp(BaseModel):
    Post: PostResponseBase
    likes: int

    class Config:
        from_attributes = True

# Login

class UserLoginResponse(UserResponseBase):
    pass

# Token

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# Vote

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)