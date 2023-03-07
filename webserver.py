import requests
while True:
    x = requests.get('http://localhost:8000')
    print(x)
