from processing.models import Message
from twilio import twiml
class Sms():
    def run(data):
        message=data.get('message')
        message = Message(**message)
        message=message.message
        response= twiml.Response()
        body=message
        response.message("You sent me: {0}".format(body))
        a=response.message("You sent me: {0}".format(body))
        print(a)