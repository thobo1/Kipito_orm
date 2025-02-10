from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from orm.database import Base
from orm.mixins import RecordTimestamps
from datetime import datetime


class Post(Base, RecordTimestamps):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    univers_id = Column(Integer, ForeignKey("univers.id"), nullable=False)

    title = Column(String, nullable=False)  # Title of the post
    description = Column(String, nullable=True)  # Description of the post
    user_rating = Column(Integer, nullable=True)  # User's rating (e.g., 1-5)
    other_ratings_count = Column(
        Integer, default=0
    )  # Count of ratings from other users
    likes = Column(Integer, default=0)  # Number of likes
    dislikes = Column(Integer, default=0)  # Number of dislikes

    user = relationship("User", back_populates="posts")
    univers = relationship("Univers", back_populates="posts")
    photos = relationship("Photo", back_populates="post", cascade="all, delete-orphan")
