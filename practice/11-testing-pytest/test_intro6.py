import requests

def test_get():
    res=requests.get("http://127.0.0.1:5000/")
    print("%$@#$%@#$%@#")
    print(res)
    assert res.status_code == 200

def test_post():
    end_url="http://127.0.0.1:5000/add"
    pay_load = {"id" :153, "name":"rdfa"}
    headers = {"content-type":"application/json"}
    res=requests.post(end_url, json=pay_load,headers=headers)
    assert res.status_code == 201