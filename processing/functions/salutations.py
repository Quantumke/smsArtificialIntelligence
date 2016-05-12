import random
class Salutations():
	def run(salutations,data):
		data['greetings']=Salutations.process_salutes(salutations)
	def process_salutes(salutations):
		salutation_one="Hello human, how can i help you"
		salutation_two="Hi there how can i be of service"
		salutation_three="Thank you for using our service, how can i help you?"
		bulk=[salutation_one,salutation_two, salutation_three ]
		greetings=random.choice(bulk)
		#print("hi!!!!!!!!!!!!!!!!!!!", greetings)
		return greetings
