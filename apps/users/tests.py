import json

import requests

web_url = "http://127.0.0.1:8888"
def test_sms():
    url = "{}/code/".format(web_url)
    data = {
        "mobile":"18821896020"
    }
    res = requests.post(url, json=data)

    print(json.loads(res.text))

if __name__=="__main__":
    test_sms()