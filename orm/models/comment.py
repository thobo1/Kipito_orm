from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm.database import Base
from orm.mixins import RecordTimestamps


class Comment(Base, RecordTimestamps):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(
        Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    content = Column(String, nullable=False)  # Content of the comment

    # Relations
    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")
