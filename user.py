import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, String, Float, DateTime
from setting import Base
from setting import ENGINE


class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', String(26), primary_key=True,
                unique=True, nullable=False)
    name = Column('name', String(), unique=True, nullable=False)
    yomi = Column('yomi', String(), nullable=True)
    state = Column('state', Boolean, default=True, nullable=False)
    last = Column('last', DateTime(), nullable=True)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
