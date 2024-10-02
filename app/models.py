from .database import Base
from sqlalchemy import Column, Integer, String,  Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean, server_default=text('TRUE'))

    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE")) #users.id iz tabele users uzima kolonu id, cascade u slucaju da roditeljska klasa se izbrise da se sve brise

    owner = relationship("User") #automatski radi posao



class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    phone_nubmer = Column(String)
class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)


