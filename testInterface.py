import requests


def insert_to_dict(dict_name: str, key: str, value: str):
    url = 'https://xxxx.com/release/manage/'
    # url = 'http://127.0.0.1:8000/dicts/manage/'  # 需要改
    data = {'dict_name': dict_name, 'key': key, 'value': value}
    response = requests.post(url, data)
    print(response)
    print("insert dict结果:", response.json())


def search_dict(dict_name, key):
    url = 'https://xxxx.com/release/insert/'
    # url = 'http://127.0.0.1:8000/dicts/insert/'
    data = {'dict_name': dict_name, 'key': key}
    response = requests.post(url, data)
    return response


insert_to_dict('ws_connections4clients', '1', '123')
res = search_dict('ws_connections4clients', None)
print("search dict结果:", res.json())
res = search_dict('ws_connections4clients', '1')
print("search dict结果:", res.json())
