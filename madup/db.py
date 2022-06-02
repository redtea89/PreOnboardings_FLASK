import os

from sqlalchemy import create_engine

PW = os.environ['MARIADB_ROOT_PASSWORD']

def madup_db_connector(app):
    engine = create_engine(
        f"mariadb+pymysql://user:{PW}@localhost/pre_flask?charset=utf8mb4"
    )