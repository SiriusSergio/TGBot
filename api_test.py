import requests

api_url = "http://numbersapi.com/43"

responce = requests.get(api_url)

if responce.status_code == 200:
    print(responce.text)
else:
    print(responce.status_code)
