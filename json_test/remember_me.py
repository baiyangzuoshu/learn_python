import json

filename='username.json'

def get_stored_username():
    try:
    	with open(filename) as f_obj:
	     username=json.load(f_obj)
    except FileNotFoundError:
    	return None
    else:
    	return username

def get_new_username():
    username=input('What is your name?')
    with open(filename,'w') as f_obj:
         json.dump(username,f_obj)
    return  username

def greet_user():
    username=get_stored_username()
    if username:
       print("Welcome back,"+username+'!')
    else:
       username=get_new_username()
       print("We'll remeber you when you come back,"+str(username)+'!')

greet_user()
