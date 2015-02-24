# coding=utf-8

import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def ejemploajaxproceso(request):
    if request.method == 'POST':
        #print request.POST
        v1 = request.POST['valorCaja1']
        v2 = request.POST['valorCaja2']
        print v1
        print v2
        r = {}
        r['resultado'] = str(int(v1) + int(v2))
        print r
        return HttpResponse(json.dumps(r), content_type="application/json")
