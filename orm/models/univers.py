from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from orm.database import Base
from sqlalchemy.orm import Session

user_univers = Table(
    "user_univers",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("univers_id", Integer, ForeignKey("univers.id")),
)


class Univers(Base):
    __tablename__ = "univers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    icon = Column(String)

    posts = relationship("Post", back_populates="univers")

    @classmethod
    def get_all_univers(cls, db: Session) -> list["Univers"]:
        """Retrieve all univers from the database."""
        return db.query(cls).all()

    @classmethod
    def exists(cls, db: Session, univers_id: int) -> bool:
        """Check if an univers exists by its ID."""
        return db.query(cls).filter(cls.id == univers_id).count() > 0
