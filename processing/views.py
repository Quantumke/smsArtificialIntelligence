from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from processing.models import *
from processing.forms import *
from processing.functions import get_message
from processing.functions import sms
from processing.functions import salutations
from processing.functions import responses
from processing.functions import sentintiment_analysis
# Create your views here.
def sendsms(request):
    context = RequestContext(request)
    message_form=form(data=request.POST)
    if request.method =='POST':
        data={}
        get_message.GetMessage.run(request,data)
        salutations.Salutations.run(request,data)
        responses.Responses.run(request, data)
        #sms.Sms.run(data)
        sentintiment_analysis.SentimentAnalysis.run(data)
        return HttpResponseRedirect('/')
    return render(request,
                  'index.html',{'form': form, },context_instance=RequestContext(request))
