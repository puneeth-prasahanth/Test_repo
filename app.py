from flask import Flask, request,jsonify
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT,jwt_required

from sample import authentication,identity
from resources.User import UserRequest
from resources.items import Item,Items

#add_resource=UserRequest

app = Flask(__name__)
app.secret_key='jame'
API = Api(app)
jwt=JWT(app,authentication,identity)




API.add_resource(Item, '/item/<string:name>')

API.add_resource(Items, '/items')

API.add_resource(UserRequest, '/request')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
