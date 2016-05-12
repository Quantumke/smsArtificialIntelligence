class GetMessage():
	def run(request_data, data):
		data['message']=GetMessage.get_message(request_data)
		#print(request_data)
	def get_message(request_data):
		message={}
		message['message']=request_data.POST.get('message')
		return message
		
