from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from orm.database import Base
import uuid


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    photo_url = Column(String, nullable=False)
    name_on_s3 = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)

    # Relation
    post = relationship("Post", back_populates="photos")
    
    def __init__(self, post_id, photo_url, name_on_s3=None):
        self.post_id = post_id
        self.photo_url = photo_url
        if name_on_s3 is not None:
            self.name_on_s3 = name_on_s3
        else:
            self.name_on_s3 = uuid.uuid4()

