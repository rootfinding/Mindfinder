from flask import request
from flask_restful import Resource
from controllers import TinderController
import logging


class Tinder(Resource):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler('app.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - Tinder - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def post(self, method):
        self.logger.info('Api post request')

        data = request.json
        if method == 'match':
            response = TinderController.match(data[0], data[1])
        if method=='agent':
            response = TinderController.agent()
        if method=='search':
            response = TinderController.search()
        if method=='feedback':
            response = TinderController.feedback()
            
        self.logger.info('Response data: ok!')
        return response, 200
