from sqlalchemy import DECIMAL, TIMESTAMP, Column
from sqlalchemy.dialects.mysql import BIGINT, FLOAT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

DEFAULT_LENGTH = 255
UnsignedInt = INTEGER(unsigned=True)
UnsignedBigInt = BIGINT(unsigned=True)
UnsignedFloat = FLOAT(unsigned=True)
STABLECOIN_TYPE = DECIMAL(18, 6)
TADA_TYPE = DECIMAL(28, 18)
TON_TYPE = DECIMAL(28, 18)


class RecordTimestamps:
    updated_at = Column(
        TIMESTAMP,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
        doc="Timestamp when the record was last updated",
    )
    created_at = Column(
        TIMESTAMP,
        default=func.now(),
        nullable=False,
        doc="Timestamp when the record was created",
    )
