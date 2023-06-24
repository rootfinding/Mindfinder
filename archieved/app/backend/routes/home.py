from flask import request
from flask_restful import Resource
import logging


class Home(Resource):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler('app.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - Home - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def post(self):
        self.logger.info('Api post request')
        self.logger.info('Response data: ok!')
        return 'ok!', 200
