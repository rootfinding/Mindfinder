from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"Access-Control-Allow-Origin": "*"}})

with app.app_context():
    import resources

api = Api(app)
resources.initialize(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
