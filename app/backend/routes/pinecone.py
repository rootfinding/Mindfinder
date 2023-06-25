from flask import request
from flask_restful import Resource
from controllers import PineconeController
import logging

class Pinecone(Resource):

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
        #                        --url http://127.0.0.1:8081/api/pinecone/upload \
        #                                               --header 'Content-Type: application/json' \
        #                                                        --data '{
        #         "text": "Hello, I'\''m Raquel, a lover of art and music. I spend my days exploring art galleries, attending concerts and enjoying the beauty of nature. Photography is another of my passions, I love capturing special moments and finding the beauty in details. I also enjoy traveling and immersing myself in different cultures. I believe that sharing similar interests is essential to building a strong connection. I am looking for someone with whom I can share deep conversations and moments filled with joy and fun. If you are passionate about art, music and exploration, I'\''d love to meet you. Swipe right if you'\''re ready to discover a world full of creativity and connection.",
        #         "metadata": {
        #             "name": "Raquel Ameri",
        #             "age": 25,
        #             "location": "Buenos Aires, Ar",
        #             "tastes": "art, music, photography, nature, and traveling",
        #             "description": "Hello, I'\''m Raquel, a lover of art and music. I spend my days exploring art galleries, attending concerts and enjoying the beauty of nature. Photography is another of my passions, I love capturing special moments and finding the beauty in details. I also enjoy traveling and immersing myself in different cultures. I believe that sharing similar interests is essential to building a strong connection. I am looking for someone with whom I can share deep conversations and moments filled with joy and fun. If you are passionate about art, music and exploration, I'\''d love to meet you. Swipe right if you'\''re ready to discover a world full of creativity and connection."
        #         },
        #         "namespace": "tinder"
        # }'
        if method == 'upload':
            if not isinstance(data['text'], str):
                return 'text is not a string', 400
            if not isinstance(data['metadata'], dict):
                return 'metadata is not a dict', 400
            if not isinstance(data['namespace'], str):
                return 'namespace is not a string', 400

            response = PineconeController.upload(data['text'], data['metadata'], data['namespace'])
            return response, 200
        #         curl --request POST \
        #                        --url http://127.0.0.1:8081/api/pinecone/query \
        #                                               --header 'Content-Type: application/json' \
        #                                                        --data '{
        #         "text": "Hello",
        #         "filter": {},
        #         "namespace": "tinder",
        #         "top_k": 2
        # }'
        elif method == 'query':
            if not isinstance(data['text'], str):
                return 'text is not a string', 400
            if not isinstance(data['filter'], dict):
                return 'metadata is not a dict', 400
            if not isinstance(data['namespace'], str):
                return 'namespace is not a string', 400
            if not isinstance(data['top_k'], int):
                return 'top_k is not an int', 400

            response = PineconeController.query(data['text'], data['filter'], data['namespace'], data['top_k'])
            return response, 200

        return [], 204
