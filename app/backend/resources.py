from routes import *


def initialize(api):
    api.add_resource(Home, '/api/home')
    api.add_resource(Pinecone, '/api/pinecone/<method>')
    api.add_resource(Tinder, '/api/tinder/<method>')
