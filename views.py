from django.http import JsonResponse, HttpResponse
import threading
import json

# 全局字典，用于存储所有其他字典
global_dicts = {}

# 并发锁
ws_lock = threading.Lock()


def manage(request):
    dict_name = request.POST.get('dict_name')
    key = request.POST.get('key')
    value = request.POST.get('value')

    if not dict_name:
        return JsonResponse({'error': 'dict_name is required'}, status=400)

    with ws_lock:
        if dict_name not in global_dicts:
            global_dicts[dict_name] = {}

        if key and value:
            global_dicts[dict_name][key] = value
            return JsonResponse({'message': 'Key-Value pair added successfully'})
        elif key:
            return JsonResponse({'value': global_dicts[dict_name].get(key, 'Key not found')})
        else:
            return JsonResponse({'error': 'Key is required to set or get a value'}, status=400)


def insert(request):
    dict_name = request.POST.get('dict_name')
    key = request.POST.get('key')

    if not dict_name:
        return JsonResponse({'error': 'dict_name is required'}, status=400)

    with ws_lock:
        if dict_name in global_dicts:
            dict_data = global_dicts[dict_name]

            if not key:
                # Return the entire dictionary
                return JsonResponse({'dict_data': dict_data})
            else:
                # Return the specific key value
                if key in dict_data:
                    return JsonResponse({'value': dict_data[key]})
                else:
                    return JsonResponse({'error': 'key not found'}, status=404)

        else:
            return JsonResponse({'message': 'dict not found'})
