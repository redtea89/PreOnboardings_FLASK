import os

from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine

from apps.madup.router import madup_router
from apps.bear.router import bear_router
from apps.human.router import human_router

app = Flask(__name__)
api = Api(app)

"""Routers"""
madup_router(api)
bear_router(api)
human_router(api)

"""DB Connector"""
PW = os.environ['MARIADB_ROOT_PASSWORD']
engine = create_engine(
    f"mariadb+pymysql://user:{PW}@localhost/pre_flask?charset=utf8mb4"
)
