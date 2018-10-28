class	Car:
	def __init__(self,make,model,year):
	    self.make=make
	    self.model=model
	    self.year=year
	    self.odometer_reading= 0
	
	def get_descriptive_name(self):
	    long_name=str(self.year)+ ' '+ self.make+' '+ self.model
	    return long_name.title()
#class Car end.
class	ElectricCar(Car):
	def __init__(self,make,model,year):
	    super().__init__(make,model,year)

#class  ElectricCar end.
