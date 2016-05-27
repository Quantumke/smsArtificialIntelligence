from processing.models import Message
from twilio import twiml
class Sms():
    def run(data):
        message=data.get('message')
        message = Message(**message)
        message=message.message
        response= twiml.Response()
        body=message
        if message=="Hello":
            greetings=data.get('greetings')
            #print(greetings)
            #response.message("message: {0}".format(body))
            #a=response.message("message: {0}".format(body))
            response.message(greetings)
            a=response.message(greetings)
            print(a)
        else:
            print ("Text help to use this service")