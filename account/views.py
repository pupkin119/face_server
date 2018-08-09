from django.http import HttpResponse, JsonResponse
# from pylint.test.functional import continue_in_finally

from .models import Clients, Client_imgs
import base64
from django.views.decorators.csrf import csrf_exempt
import pathlib
import shutil
from django.utils import timezone

# httpAdress = 'http://127.0.0.1:8000/v2222/account/authentication/'

dicError = {'NoError': {'error': '0'}, 'InvalidAuthKey': {'error': '10'}, 'ClientNotFound': {'error': '20'},
            'RestaurantNotFound': {'error': '21'}, 'ImageNotValid': {'error': '22'},'AuthError': {'error': '30'},
           'ClientImageEncodeNotFound': {'error': '31'}}

# def Index(request): #Дефаутный индекс
# #     return render(request, 'account/index.html')

def verificationKey(authKey):
    # TODO authKey
    return 1

# Коды ошибок
# 10 - Неверный ключ auth key
# 20 - Клиент не найден
# 21 - Ресторан не найден
# 22 - Не валидное изображение
# 30 - Ошибка аутентификации
# 31 - Клиент с таким encoded_image не найден

# def sendError(errorName):
# #     http = urllib3.PoolManager()
# #     http.request('POST', httpAdress, fields={"error ": errorName,})

@csrf_exempt
def addNewId(request):
    if request.method == 'POST':
        if not(verificationKey(request.POST['auth_key'])):
            return JsonResponse({'error': '10'})

        client_id = request.POST['client_id']
        restaurant_id = request.POST['restaurant_id']
        encoded_image = request.POST['encoded_image']
        time_now = timezone.now()
        try:
            co = Clients.objects.get(client_id=request.POST['client_id'])
        except(Clients.DoesNotExist):
            c = Clients()
            c.client_id = client_id
            c.restaurant_id = restaurant_id

            c.created_at = time_now
            c.updated_at = time_now
            c.save()

            filename = 'Database/' + client_id + '/' + client_id + '_' + str(time_now) + '.jpg'

            ci = Client_imgs(id=None, image_path=filename, client_id=c)
            ci.save()
        else:
            co = Clients.objects.get(client_id=request.POST['client_id'])
            co.updated_at = time_now
            co.save()

            filename = 'Database/' + client_id + '/' + client_id + '_' + str(time_now) + '.jpg'
            ci = Client_imgs(id=None, image_path=filename, client_id=co)
            ci.save()

        pathlib.Path('Database/' + client_id).mkdir(parents=True, exist_ok=True)
        filename = 'Database/' + client_id + '/' + client_id + '_' + str(time_now) + '.jpg'

        with open(filename, "wb") as fh:
            fh.write(base64.standard_b64decode(encoded_image))
    return JsonResponse({'error': '0'})

@csrf_exempt
def deleteId(request, client_id):
    if request.method == 'DELETE':
        try:
            c = Clients.objects.get(client_id=client_id)
        except(Clients.DoesNotExist):
            return JsonResponse({'error': '20'})
        else:
            shutil.rmtree('Database/' + str(client_id), ignore_errors=True)
            c.delete()
    return JsonResponse({'error': '0'})

@csrf_exempt
def editId(request, client_id):
    # if request.method == 'POST':
    #     if not(verificationKey(request.POST['auth_key'])):
    #         sendError(dic['InvalidAuthKey'])
    #         return HttpResponse('no')
    #
    #     client_id_new = request.POST['client_id']
    #     restaurant_id_new = request.POST['restaurant_id']
    #     encoded_image_new = request.POST['encoded_image']
    #
    #     try:
    #         my_record = Clients.objects.get(client_id = client_id)
    #     except(Clients.DoesNotExist):
    #         sendError(dic['ClientNotFound'])
    #         return HttpResponse('no')
    #     else:
    #         shutil.rmtree('testAlign/' + str(client_id), ignore_errors=True)
    #
    #         pathlib.Path('testAlign/' + client_id_new).mkdir(parents=True, exist_ok=True)
    #         filename = 'testAlign/' + client_id_new + '/1.jpg'
    #
    #         with open(filename, "wb") as fh:
    #             fh.write(base64.standard_b64decode(encoded_image_new))
    #
    #         my_record.client_id = client_id_new
    #         my_record.restaurant_id = restaurant_id_new
    #         # my_record.encoded_image = encoded_image_new
    #         my_record.save()
    #
    #
    #
    #         sendError(dic['NoError'])
    return HttpResponse ('yes')

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