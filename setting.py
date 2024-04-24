from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

pymysql.install_as_MySQLdb()

# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    os.getenv("DB_USER"),
    os.getenv("DB_PASS"),
    os.getenv("DB_HOST"),
    os.getenv("DB_NAME")
)
ENGINE = create_engine(
    DATABASE,
)

# Sessionの作成
session = scoped_session(
    sessionmaker(
        autoflush=True,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
