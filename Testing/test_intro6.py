import requests

def test_get():
    res=requests.get("http://127.0.0.1:5000/")
    print("%$@#$%@#$%@#")
    print(res)
    assert res.status_code == 200
test_get()