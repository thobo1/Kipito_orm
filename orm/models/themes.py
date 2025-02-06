from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from orm.database import Base
from sqlalchemy.orm import Session

user_themes = Table(
    "user_themes",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("theme_id", Integer, ForeignKey("themes.id")),
)


class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    icon = Column(String)

    posts = relationship("Post", back_populates="theme")

    @classmethod
    def get_all_themes(cls, db: Session):
        """Retrieve all themes from the database."""
        return db.query(cls).all()
