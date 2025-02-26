from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm.database import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_id = Column(
        Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )

    # Relations
    user = relationship("User", back_populates="bookmarks")
    post = relationship("Post", back_populates="bookmarks")
