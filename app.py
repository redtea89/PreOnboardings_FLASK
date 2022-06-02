from flask import Flask

from flask_restful import Api

from madup.router import madup_router
from madup.db import madup_db_connector

app = Flask(__name__)
api = Api(app)

madup_db_connector(app)
madup_router(api)
