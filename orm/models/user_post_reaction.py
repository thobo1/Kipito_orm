from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from orm.database import Base
import enum


class ReactionType(enum.Enum):
    LIKE = "like"
    DISLIKE = "dislike"


class UserPostReaction(Base):
    __tablename__ = "user_post_reactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_id = Column(
        Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
    reaction = Column(Enum(ReactionType), nullable=False)
    user = relationship("User", back_populates="reactions")
    post = relationship("Post", back_populates="reactions")
