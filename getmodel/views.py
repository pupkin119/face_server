from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import os

import hashlib

def generateUrl():
    #TODO generate url for model
    return 'https://face.jowi.club'

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

@csrf_exempt
def getModel(request):
    if request.method == "GET":
        url = generateUrl()
        md5Str = md5Checksum(os.path.dirname(os.path.abspath(__file__)) + '/1.jpg')
        return JsonResponse({'error': '0', 'file_url': str(url), 'file_md5': md5Str})