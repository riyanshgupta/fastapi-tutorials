# MVC = Model Views Controllers
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
    
class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String, nullable=True)
    desc = Column(String, nullable=True)
    likes = Column(Integer, default=0, nullable=False)
    
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    author = relationship("User", back_populates="posts")
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashedpassword = Column(String(255), unique=True, nullable=False)
    
    posts = relationship("Posts", back_populates="author", cascade='all, delete')