# Registration
# 1) User name
# 2) Nickname
# 3) Password
# 4) Email

# Exit 

#Registration

############### functions #####
def registration (user_name , nickname , password , email, data_base) :  
        return {
          "user_name" : user_name,
          "nickname" : nickname,
          "password" : password,
          "email" : email
      }

def name_is_valid (name_value) :
    if len(name_value) < 3 or len(name_value) > 13 :
        print("Invalid name")
        return False 
    else:    
        return True

def nickname_is_valid (nickname_value) :
    if len(nickname_value) < 4 or len(nickname_value) > 10 :
        print("Invalid nickname")
        return False
    else :
        return True

def password_is_valid (password_value) :
    if len(password_value) < 8 or len(password_value) > 12 :
        print("Invalid password")
        return False
    else :
        return True

def email_is_valid (email_value) :
    if "@" in email :
        return True
    else :
        print("Invalid email") 
        return False
  
def auth (nickname_value, password_value, data_base_value):
    for item in data_base_value:
        if item['nickname']==nickname_value and item['password']==password_value :
            return "Glad to see you " +  nickname_value

    return "Try again"  
###############################

data_base = []
user = {}
 

data_base = [
    {
        "user name" : "alexander",
        "nickname" : "alex",
        "password" : "5656565656",
        "email" : "alex@gm.ua"
    }, 
    {
        "user name" : "maria",
        "nickname" : "candy",
        "password" : "34673467",
        "email" : "mari@gm.ua"
    } ,
    {
        "user name" : "carolina",
        "nickname" : "carolina",
        "password" : "123456789",
        "email" : "car@gm.ua"
    }
] 

exit_symbol = ''
is_authorized = False

while exit_symbol.lower() != 'x' and is_authorized==False:
    user_name = input("Enter your name (3 - 13 symbols) : " )
    nickname = input("Enter your nickname (4 - 10 symbols): ")
    password = input("Enter your password (8 - 12 symbols) : ")
    email = input("Enter your email (must contain @): ")
    if name_is_valid(user_name) and  nickname_is_valid(nickname) and password_is_valid (password) and email_is_valid(email) :
        is_authorized=True
        print("User is authorized successfully" )
    else :   
        exit_symbol = input('If You want to exit - press "x": ')
        

if is_authorized == False :           
    exit(0)         


# Authorization
print(auth (nickname, password, data_base))
for user in data_base :
    for key , value in user.items() :
        print(key, value)

user = data_base
data_base.append({ "nickname" : nickname,
        "password" : password}) 
print(data_base)                                      