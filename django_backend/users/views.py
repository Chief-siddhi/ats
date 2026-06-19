from django.http import JsonResponse
import requests



def users_list(request):

    response=requests.get(
        "http://127.0.0.1:8001/users"
    )

    data=response.json()

    return JsonResponse(
        data,
        safe=False
    )