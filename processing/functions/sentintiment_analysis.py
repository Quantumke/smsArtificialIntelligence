from processing.models import Message
from twilio import twiml
from textblob import TextBlob

class SentimentAnalysis():
    def run(data):
        message= data.get('message')
        message=Message(**message)
        message=message.message
        response = twiml.Response()
        responses=data.get('responses')
        good=responses.get('good')
        bad=responses.get('bad')
        neutral=responses.get('neutral')
        text=TextBlob(message)
        sentiment = text.sentiment
        if sentiment.polarity > 0:
            response.message(good)
            a=responses.message(good)
            print(a)
        elif sentiment.polarity < 0:
            response.message(bad)
            b=response.message(bad)
            print(b)
        else:
            response.message(neutral)
            b=response.message(neutral)
            print(b)
        return str(response)
