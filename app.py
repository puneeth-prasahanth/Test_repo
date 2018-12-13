from flask import Flask, request,jsonify
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT,jwt_required

from sample import authentication,identity
from resources.User import UserRequest
from resources.items import Item,Items
from creata_table import create_tables

#add_resource=UserRequest

app = Flask(__name__)
app.secret_key='jame'
API = Api(app)

@app.before_first_request
def create_tables_method():
    create_tables.tables_creation()

jwt=JWT(app,authentication,identity)




API.add_resource(Item, '/item/<string:name>')

API.add_resource(Items, '/items')

API.add_resource(UserRequest, '/request')

if __name__ == '__main__':
    from creata_table import create_tables
    #create_tables._init_app(app)
    create_tables_method()
    app.run(port=5000, debug=True)
