import json
numbers=[12,15,3,5,96]

filename='numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

with open(filename) as f_obj:
	message=f_obj.read()
	print(message)
