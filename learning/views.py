from django.shortcuts import render
from django.http import HttpResponse
from account.models import CreateId
import urllib3
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from  shutil import copyfile

from pathlib import Path

from .models import WriteErrorToDb


# Create your views here.
httpAdress = 'http://127.0.0.1:8000/v2222/account/authentication/'

dic = {'NoError': 0, 'InvalidAuthKey': 10, 'ClientNotFound': 20, 'RestaurantNotFound': 21, 'ImageNotValid': 22, 'AuthError': 30,
      'ClientImageEncodeNotFound': 31}

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
def statrtLearning(request):
    if request.method == 'POST':
        if not(verificationKey(request.POST['auth_key'])):
            sendError(dic['InvalidAuthKey'])
            return HttpResponse('no')
        my_record_count = CreateId.objects.count()
        my_record_ids = CreateId.objects.only('client_id')

        for i in np.arange(my_record_count):
            my_file = Path("faceVerification/" + str(my_record_ids[int(i)].client_id) + ".jpg")
            if my_file.is_file():
                continue
            else:
                try:
                    copyfile('testAlign/' + str(my_record_ids[int(i)].client_id) + '/1.jpg', 'faceVerification/' + str(my_record_ids[int(i)].client_id) + '.jpg')
                except FileNotFoundError:
                    q = WriteErrorToDb()
                    q.module = 'startLearning'
                    q.client_id = my_record_ids[int(i)].client_id
                    q.error_id = 41
                    q.save()
                else:
                    continue

        sendError(dic['NoError'])
    return HttpResponse('yes')