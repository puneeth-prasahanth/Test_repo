import sqlite3


class ItemModel:

    def __int__(self,name,prize):
        self.name=name
        self.prize=prize

    @classmethod
    def selection(cls,name):
        connection=sqlite3.connect('item.db')
        con_cur=connection.cursor()
        select_statment="select * from items where item=?"
        selection=con_cur.execute(select_statment,(name,))
        result=selection.fetchone()
        connection.commit()
        connection.close()
        return result

    @classmethod
    def updation(cls,*args):
        connection=sqlite3.connect('item.db')
        con_cur=connection.cursor()
        arg_count=len(args)
        name=args[0]
        prize=args[1]
        print(f'name:{name},prize:{prize}')
        if args[2] == 1 :
            update_statment=f'update items set prize={prize} where item=\'{name}\''
        elif args[2] == 0 :
            update_statment=f'insert into items values(\'{name}\',{prize})'
        print (name,prize)
        print(f'update_statment:{update_statment}')
        updation=con_cur.execute(update_statment)
        connection.commit()
        connection.close()


