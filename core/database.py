"""
Database Connection & Engine Creation
"""

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from core.constants import Constants

# LOCAL
# engine = create_engine(Constants.SQLALCHAMY_DATABASE_URL)

# REMOTE 
# engine = create_engine(
#      URL.create(
#             drivername="mysql+pymysql",
#             username=Constants.tidb_username,
#             password=Constants.tidb_password,
#             host=Constants.tidb_db_host,
#             port=Constants.tidb_port,
#             database=Constants.tidb_database
#         ),
#         connect_args={},
# )
engine = create_engine(Constants.TIDB_SQLALCHAMY_DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


def get_db():
    """Get Database Instance"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
