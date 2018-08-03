from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpRequest
from .models import CreateId
import base64
import urllib3
from django.views.decorators.csrf import csrf_exempt
import pathlib
import shutil

httpAdress = 'http://127.0.0.1:8000/v2222/account/authentication/'

dic = {'NoError': 0, 'InvalidAuthKey': 10, 'ClientNotFound': 20, 'RestaurantNotFound': 21, 'ImageNotValid': 22, 'AuthError': 30,
      'ClientImageEncodeNotFound': 31}



from django.db import models

# Create your views here.

# def Index(request): #Дефаутный индекс
# #     return render(request, 'account/index.html')

def verificationKey(authKey):
    # TODO
    return 1

# Коды ошибок
# 10 - Неверный ключ auth key
# 20 - Клиент не найден
# 21 - Ресторан не найден
# 22 - Не валидное изображение
# 30 - Ошибка аутентификации
# 31 - Клиент с таким encoded_image не найден
def sendError(errorName):
    http = urllib3.PoolManager()
    http.request('POST', httpAdress, fields={"error ": errorName,})


@csrf_exempt
def addNewId(request):
    if request.method == 'POST':
        if not(verificationKey(request.POST['auth_key'])):
            sendError(dic['InvalidAuthKey'])
            return HttpResponse('no')

        client_id = request.POST['client_id']
        restaurant_id = request.POST['restaurant_id']
        encoded_image = request.POST['encoded_image']
        q = CreateId()
        q.client_id = client_id
        q.restaurant_id = restaurant_id
        q.encoded_image = encoded_image
        q.save()

        pathlib.Path('testAlign/' + client_id).mkdir(parents=True, exist_ok=True)
        filename = 'testAlign/' + client_id + '/1.jpg'

        with open(filename, "wb") as fh:
            fh.write(base64.standard_b64decode(encoded_image))
        sendError(dic['NoError'])
    return HttpResponse('yes')

@csrf_exempt
def editId(request, client_id):
    if request.method == 'GET':
        if not(verificationKey(request.POST['auth_key'])):
            sendError(dic['InvalidAuthKey'])
            return HttpResponse('no')

        client_id_new = request.POST['client_id']
        restaurant_id_new = request.POST['restaurant_id']
        encoded_image_new = request.POST['encoded_image']

        try:
            my_record = CreateId.objects.get(client_id = client_id)
        except(CreateId.DoesNotExist):
            sendError(dic['ClientNotFound'])
            return HttpResponse('no')
        else:
            shutil.rmtree('testAlign/' + str(client_id), ignore_errors=True)

            pathlib.Path('testAlign/' + client_id_new).mkdir(parents=True, exist_ok=True)
            filename = 'testAlign/' + client_id_new + '/1.jpg'

            with open(filename, "wb") as fh:
                fh.write(base64.standard_b64decode(encoded_image_new))

            my_record.client_id = client_id_new
            my_record.restaurant_id = restaurant_id_new
            my_record.encoded_image = encoded_image_new
            my_record.save()

            sendError(dic['NoError'])
    return HttpResponse ('yes')

@csrf_exempt
def deleteId(request, client_id):
    if request.method == 'GET':
        if not(verificationKey(request.GET['auth_key'])):
            sendError(dic['InvalidAuthKey'])
            return HttpResponse('no')

        q = CreateId.objects.get(client_id = client_id)
        shutil.rmtree('testAlign/' + str(client_id), ignore_errors=True)
        q.delete()

        sendError(dic['NoError'])

    return HttpResponse('yes')

# @csrf_exempt
# def authentication(request):
#     if request.method == 'POST':
#         if not(verificationKey(request.POST['auth_key'])):
#             sendError(dic['InvalidAuthKey'])
#         client_id = request.POST['client_id']
#         restaurant_id = request.POST['restaurant_id']
#         encoded_image = request.POST['encoded_image']
#         try:
#             my_record = CreateId.objects.get(client_id=client_id, restaurant_id=restaurant_id,
#                                                  encoded_image=encoded_image)
#         except(KeyError, CreateId.DoesNotExist):
#             sendError(dic['AuthError'])
#             return HttpResponse('no')
#         else:
#             sendError(dic['NoError'])
#             return HttpResponse('yes')
#     return HttpResponse('no')