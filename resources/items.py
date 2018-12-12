from flask import Flask, request,jsonify
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT,jwt_required
import sqlite3
from models.items import ItemModel

class Item(Resource):

    @jwt_required()
    def get(self, name):

        RC=ItemModel.selection(name)

        if RC:
            return{"items" : {"name":RC[0],"prize":RC[1]}}
        else:
            return{"message":"no data available for "+name}
        #return {"message":"User created successfully :)" },201

        #single_item = next(filter(lambda x: x['name'] == name, item),None)
        #return {'Item':single_item},200 if single_item else 404#200 success req, 404

    def delete(self,name):
        connection=sqlite3.connect('item.db')
        con_cur=connection.cursor()
        delete_statment="delete from items where item=?"
        deletion=con_cur.execute(delete_statment,(name,))
        connection.commit()
        connection.close()

    def put(self,name):

        parser=reqparse.RequestParser()
        parser.add_argument('prize',
                            type=float,
                            required=True,
                            help="Prize is mandit bro :)")

        data=parser.parse_args()
        #data=request.get_json()
        RC=ItemModel.selection(name)
        if RC:

            ItemModel.updation(RC[0],data['prize'],1)
            return{'Message':name +' item already Exists updated it with latest prize ' },201 # bad request
        else:
            ItemModel.updation(name,data['prize'],0)
            return{'Message':name + ' item updated successfully '},201 # bad request

    def post(self, name):

        parser=reqparse.RequestParser()
        parser.add_argument('prize',
                            type=float,
                            required=True,
                            help="Prize is mandit bro :)")
        data=parser.parse_args()
        RC=ItemModel.selection(name)
        if RC:
            return{'Message':name+' item already Exists'},400# bad request
        else:
            ItemModel.updation(name,data['prize'],0)
            #Ite={'name':name,'prize':data['prize']}
            #item.append(Ite)
            return {"item":{"name":name,"prize":data['prize']}},201 #201 Successfull Posted



class Items(Resource):
    def get(self):
        connection=sqlite3.connect('item.db')
        con_cur=connection.cursor()
        select_statment="select * from items "
        selection=con_cur.execute(select_statment)
        #result=selection.fetchone()
        #return {"items":({val[0]:val[1]} for val in selection) }
        items={"items":[{val[0]:val[1] for val in selection}]}
        connection.commit()
        connection.close()
        return jsonify(items)
