from flask import Flask
from flask_restful import Resource, Api
from bip_scrapper import get_balance
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class BipBalance(Resource):
    def get(self, card_id):
        return get_balance(card_id)

api.add_resource(BipBalance, '/bip/balance/<string:card_id>')

if __name__ == '__main__':
    app.run(debug=True)
