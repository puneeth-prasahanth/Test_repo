import sqlite3

from flask_restful import Resource,reqparse


class UserRequest(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                            type=str,
                            required=True,
                            help="username is mandit bro :)")
    parser.add_argument('password',
                            type=str,
                            required=True,
                            help="password is mandit bro :)")

    def post(self):
        data=UserRequest.parser.parse_args()

        if user.db_validate(data['username']):
            return {"message":"User already exists"}
        connection=sqlite3.connect('data.db')
        con_cur=connection.cursor()
        insert_statment="insert into users values(NULL,?,?)"
        insertion=con_cur.execute(insert_statment,(data['username'],data['password']))

        connection.commit()
        connection.close()
        return {"message":"User created successfully :)" },201


