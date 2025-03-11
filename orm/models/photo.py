from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from orm.database import Base
import uuid


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    name_on_s3 = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    file_type = Column(String, default="jpg", nullable=False)
    # Relation
    post = relationship("Post", back_populates="photos")
