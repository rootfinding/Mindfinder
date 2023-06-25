from flask import request
from flask_restful import Resource
from controllers import TinderController, PineconeController
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
        data = request.json
        #         curl --request POST \
        #                        --url http://127.0.0.1:8081/api/tinder/match \
        #                                               --header 'Content-Type: application/json' \
        #                                                        --data '{
        #         "name": "Raquel Ameri",
        #         "age": 25,
        #         "location": "Buenos Aires, Ar",
        #         "tastes": "art, music, photography, nature, and traveling",
        #         "description": "Hello, I'\''m Raquel, a lover of art and music. I spend my days exploring art galleries, attending concerts and enjoying the beauty of nature. Photography is another of my passions, I love capturing special moments and finding the beauty in details. I also enjoy traveling and immersing myself in different cultures. I believe that sharing similar interests is essential to building a strong connection. I am looking for someone with whom I can share deep conversations and moments filled with joy and fun. If you are passionate about art, music and exploration, I'\''d love to meet you. Swipe right if you'\''re ready to discover a world full of creativity and connection."
        # }'
        if method == 'match':
            if not isinstance(data['name'], str):
                return 'name is not a string', 400
            if not isinstance(data['description'], str):
                return 'description is not a string', 400

            query_results = PineconeController.query(data['description'], {
                "name": {"$ne": data['name']},
            }, 'tinder', 1)

            if len(query_results['matches']) == 0:
                response = TinderController.match(data)
                return response, 200

            print("Simulating" + query_results['matches'][0]['metadata']['name'])
            response = TinderController.match(data, query_results['matches'][0]['metadata'])
            return response, 200
        #           curl --request POST \
        #               --url http://127.0.0.1:8081/api/tinder/match_chandler \
        #                                      --header 'Content-Type: application/json' \
        #                                               --data '{
        #           "name": "Raquel Ameri",
        #           "age": 25,
        #           "location": "Buenos Aires, Ar",
        #           "tastes": "art, music, photography, nature, and traveling",
        #           "description": "Hello, I'\''m Raquel, a lover of art and music. I spend my days exploring
        #               art galleries, attending concerts and enjoying the beauty of nature. Photography is
        #               another of my passions, I love capturing special moments and finding the beauty in details.
        #               I also enjoy traveling and immersing myself in different cultures. I believe that sharing
        #               similar interests is essential to building a strong connection. I am looking for someone
        #               with whom I can share deep conversations and moments filled with joy and fun. If you are
        #               passionate about art, music and exploration, I'\''d love to meet you. Swipe right if
        #               you'\''re ready to discover a world full of creativity and connection."
        #       }'
        elif method == 'match_chandler':
            if not isinstance(data['name'], str):
                return 'name is not a string', 400
            if not isinstance(data['description'], str):
                return 'description is not a string', 400

            response = TinderController.match_chandler(data)
            return response, 200
            
        return [], 204
