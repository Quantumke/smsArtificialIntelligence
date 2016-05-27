class Responses():
	def run(request_responses,data):
		data['responses']=Responses.get_responses(request_responses)
	def get_responses(request_responses):
		responses={}
		responses['good']="Thats good to hear. Do you need extra help"
		responses['neutral']="Thank you for you info how can we help you?"
		responses['bad']="We are sorry for the incovininces how can we help you?"
		return responses
