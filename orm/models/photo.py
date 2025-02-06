from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm.database import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    photo_url = Column(String, nullable=False)

    # Relation
    post = relationship("Post", back_populates="photos")
