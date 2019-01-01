from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from parking.User import User
@csrf_exempt
def api_login(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':

        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            user = User()
            result = User.Login(user, data)
            if result == 1:
                return JsonResponse(data={'msg': 'SUCCESSED'}, status=status.HTTP_200_OK)
            return JsonResponse(data={'msg': 'FAILED'}, status=status.HTTP_200_OK)

    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])
@csrf_exempt
def api_register(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':

        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            user = User()
            result = User.Register(user, data)
            if result == 1:
                return JsonResponse(data={'msg': 'SUCCESSED'}, status=status.HTTP_200_OK)
            return JsonResponse(data={'msg': 'username existed'}, status=status.HTTP_200_OK)

    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])

