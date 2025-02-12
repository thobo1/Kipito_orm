from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
    Table,
)
from orm.database import Base
from orm.mixins import RecordTimestamps
from orm.types import DEFAULT_LENGTH
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from .univers import user_univers


user_followers = Table(
    "user_followers",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("followed_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class User(Base, RecordTimestamps):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(DEFAULT_LENGTH), unique=True, nullable=False)
    hashed_password = Column(String(DEFAULT_LENGTH), nullable=False)
    is_active = Column(Boolean, default=False)
    is_onboarding = Column(Boolean, default=False)
    otp_code = Column(String(6), nullable=True)
    otp_valid_until = Column(DateTime, nullable=True)
    name = Column(String(DEFAULT_LENGTH), unique=True)
    lastname = Column(String(DEFAULT_LENGTH), unique=True)
    bio = Column(Text, nullable=True)  # Courte biographie
    profile_picture = Column(String, nullable=True)  # URL de la photo de profil
    # location = Column(
    #     String(DEFAULT_LENGTH), nullable=True
    # )  # Localisation (ex: Barcelone, Espagne)
    posts_count = Column(Integer, default=0)  # Nombre de posts
    followers_count = Column(Integer, default=0)  # Nombre de followers
    following_count = Column(Integer, default=0)  # Nombre de suivis
    popularity_score = Column(Integer, default=0)  # Score de popularité

    preferred_univers = relationship(
        "Univers", secondary=user_univers, backref="users", lazy="dynamic"
    )
    posts = relationship("Post", back_populates="user")
    reactions = relationship("UserPostReaction", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    followers = relationship(
        "User",
        secondary=user_followers,
        primaryjoin=id == user_followers.c.followed_id,
        secondaryjoin=id == user_followers.c.follower_id,
        backref="following",
    )

    def __repr__(self):
        return f"<User(email={self.email}, is_active={self.is_active})>"

    @classmethod
    def get_by_email(cls, db: Session, email: str) -> "User":
        return db.query(cls).filter(cls.email == email).first()
