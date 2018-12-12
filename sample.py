from models.Users import UserModel

#user= user
#user=user.user


#users=[
#    user.db_validate(1,"normal","secrate")
#]
#
#print (f'users:{users}')
#for i in users:
#    print (f'i:{i["username"]}')
#    print (f'i:{i["id"]}')
#    #print (f'i:{i.username}')
#    #print (f'i:{i.get("username","none")}')
#
#username_mapping={u["username"]: u for u in users}
#
#userid_mapping={u["id"]: u for u in users}

def authentication(username,password):
    print(f'username:{username}')
    User=UserModel.db_validate(username)
    print (f'username:{User},password:{password}')
    if User and User.password == password:
        print (f'User:{User.password}')
        return User

def identity(payload):
    print(f'here in payload{payload}')
    user_id=payload['identity']
    print(f'user_id:{user_id}')
    return UserModel.id_validate(user_id)
