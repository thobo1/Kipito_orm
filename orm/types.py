from sqlalchemy import DECIMAL
from sqlalchemy.dialects.mysql import BIGINT, FLOAT, INTEGER

DEFAULT_LENGTH = 255
UnsignedInt = INTEGER(unsigned=True)
UnsignedBigInt = BIGINT(unsigned=True)
UnsignedFloat = FLOAT(unsigned=True)
STABLECOIN_TYPE = DECIMAL(18, 6)
TADA_TYPE = DECIMAL(28, 18)
TON_TYPE = DECIMAL(28, 18)
