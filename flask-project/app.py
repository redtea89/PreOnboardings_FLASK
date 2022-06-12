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
try:
    from local_settings import USER, HOST, PASSWORD
except:
    USER = os.environ['AZURE_MYSQL_USER']
    HOST = os.environ['AZURE_MYSQL_HOST'],
    PASSWORD = os.environ['AZURE_MYSQL_PASSWORD']

engine = create_engine(
    f"mariadb+pymysql://{USER}:{PASSWORD}@{HOST}/pre_flask?charset=utf8mb4"
)