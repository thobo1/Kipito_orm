from sqlalchemy import Boolean, Column, Integer, String, DateTime
from ..database import Base
from ..mixins import RecordTimestamps
from ..types import DEFAULT_LENGTH


class User(Base, RecordTimestamps):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(DEFAULT_LENGTH), unique=True, nullable=False)
    hashed_password = Column(String(DEFAULT_LENGTH), nullable=False)
    is_active = Column(Boolean, default=False)
    otp_code = Column(String(6), nullable=True)
    otp_valid_until = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<User(email={self.email}, is_active={self.is_active})>"
