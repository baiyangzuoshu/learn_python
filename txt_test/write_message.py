filename='programming.txt'
#'w','r','a','r+'
with open(filename,'w') as file_object:
	file_object.write('I Love programming.\n')

with open(filename,'a') as file_object:
	file_object.write('I love jiaer.\n')

