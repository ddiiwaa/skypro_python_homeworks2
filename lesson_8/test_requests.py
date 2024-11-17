import requests

def test_simple_req():
    resp = requests.get ('https://httpbin.org/basic-auth/user/pass')
    
    response_body = resp.json()

    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "appiication/json"