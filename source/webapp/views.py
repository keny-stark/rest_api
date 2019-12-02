import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index_view(request, *args, **kwargs):
    return render(request, 'index.html')


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            try:
                number_for_result = json.loads(request.body)
                result = (int(number_for_result['A']) + int(number_for_result['B']))
                answer = {'content': result}
                return JsonResponse(answer)
            except ValueError:
                    response = JsonResponse({'error': 'No data provided!'})
                    response.status_code = 400
                    return response


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            try:
                number_for_result = json.loads(request.body)
                result = (int(number_for_result['A']) - int(number_for_result['B']))
                answer = {'content': result}
                return JsonResponse(answer)
            except ValueError:
                    response = JsonResponse({'error': 'No data provided!'})
                    response.status_code = 400
                    return response


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            try:
                number_for_result = json.loads(request.body)
                result = (int(number_for_result['A']) * int(number_for_result['B']))
                answer = {'content': result}
                return JsonResponse(answer)
            except ValueError:
                response = JsonResponse({'error': 'No data provided!'})
                response.status_code = 400
                return response


@csrf_exempt
def divide_view(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            if request.body:
                try:
                    number_for_result = json.loads(request.body)
                    result = (int(number_for_result['A']) // int(number_for_result['B']))
                    answer = {'content': result}
                    return JsonResponse(answer)
                except ZeroDivisionError:
                        response = JsonResponse({'error': 'No data provided!'})
                        response.status_code = 400
                        return response
    except ValueError:
        response = JsonResponse({'error': 'No data provided!'})
        response.status_code = 400
        return response
