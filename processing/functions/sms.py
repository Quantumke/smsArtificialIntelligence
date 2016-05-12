from processing.models import Message
from twilio import twiml
class Sms():
    def run(data):
        message=data.get('message')
        message = Message(**message)
        message=message.message
        response= twiml.Response()
        body=message
        greetings=data.get('greetings')
        #print(greetings)
        #response.message("message: {0}".format(body))
        #a=response.message("message: {0}".format(body))
        a=response.message(greetings)
        print(a)