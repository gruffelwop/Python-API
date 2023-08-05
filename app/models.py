from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, primary_key=False, nullable=False)
    content = Column(String, primary_key=False, nullable=False)
    published = Column(Boolean, primary_key=False, nullable=False, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))
    user_id = Column(Integer,
                     ForeignKey(
                         "users.id",
                         ondelete="CASCADE",
                        #  ondelete="NO ACTION",
                        #  onupdate="NO ACTION",
                    ),
                    primary_key=False,
                    nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, primary_key=False, nullable=False, unique=True)
    password = Column(String, primary_key=False, nullable=False, unique=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

class Vote(Base):
    __tablename__ = "votes"
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, nullable=False)