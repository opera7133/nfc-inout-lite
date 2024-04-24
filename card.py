import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from setting import Base
from setting import ENGINE


class Card(Base):
    """
    カードモデル
    """
    __tablename__ = 'cards'
    id = Column('id', String(26), primary_key=True,
                unique=True, nullable=False)
    idm = Column('idm', String(16), unique=True, nullable=False)
    name = Column('name', String(), nullable=True)
    userId = Column('userId', String(26), nullable=False)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
