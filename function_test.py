def describe_pet(animal_type,pet_name):
    print(animal_type,pet_name)

describe_pet('hamster','harry')
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

message=['name','maomao','age',18]
mess=message[:]
mess.append('jiaer')
print(message,mess)

def make_pizza(*toppings):
    print(toppings)

make_pizza('maomao','jiaer','zoukai')

def make_pizza_two(size,*toppings):
    print(size,toppings)

make_pizza_two(999,'self','me','she')

def build_profile(first,last,**user_info):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_info=build_profile('albert','einstein',location='princeton',field='physics')
print(user_info)
