# from urllib import request, parse, error
# 코드로 http 요청을 하는 클라언트
# import json

import requests
res = requests.get('https://httpbin.org/get',
                   params={'q': 'python'})
print(res.json())

if __name__=="__main__":
    # query = parse.urlencode({'q': 'python'})

    # # httpbin은 요청 내용을 반환해 줌
    # url = f'https://httpbin.org/get?{query}'
    # print(url) #https://httpbin.org/get?q=python
    # try:
    #     with request.urlopen(url) as f:
    #         res = f.read().decode('utf-8')
    #         print(res)
    #         print(type(res))
    # except error.HTTPError as e:
    #     print(e)

    # print(json.loads(res))

    res = requests.get('https://httpbin.org/get',
                   params={'q': 'python'})
    print(res.json())

    res = requests.post('https://httpbin.org/post',data={'q': 'python'})    
    print(res.json().keys())
    res.json()['form']