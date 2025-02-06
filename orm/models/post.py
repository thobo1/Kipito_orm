from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from orm.database import Base
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relations
    user = relationship("User", back_populates="posts")
    theme = relationship("Theme", back_populates="posts")
    photos = relationship("Photo", back_populates="post", cascade="all, delete-orphan")
