import sqlite3

class UserModel:

    def __init__(self,_id,username,password):
        #print(f'In Class')
        self.id=_id
        self.username=username
        self.password=password


    @classmethod
    def db_validate(cls,username):
        # type: (object, object) -> object
        """

        :param _id:
        :param username:
        :return:
        """
        connection=sqlite3.connect('data.db')
        con_cur=connection.cursor()

        print (f'username:{username}')
        select_statment=f'select * from users where username =? '
        print (f'select_statment:{select_statment}')
        exc = con_cur.execute(select_statment,(username,))
        x = exc.fetchone()

        if x:
            print (f'{x}')
            ret = cls(*x)
        else:
            ret = None

        connection.close()
        return ret

    @classmethod
    def id_validate(cls,_id):
        # type: (object, object) -> object
        """

        :param _id:
        :return:
        """
        connection=sqlite3.connect('data.db')
        con_cur=connection.cursor()
        print (f'id:{id}')
        select_statment=f'select * from users where id=? '
        print (f'select_statment:{select_statment}')
        exc=con_cur.execute(select_statment,(_id,))
        x=exc.fetchone()

        if x:

            ret = cls(*x)
        else:
            ret = None

        connection.close()
        return ret
