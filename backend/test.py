import requests

BASE = "http://127.0.0.1:5000/"

response=requests.get(BASE + "user/1")
print(response.json())
input()

response = requests.put(BASE + "user/2", {"name": "james"})
print(response.json())
input()

response=requests.get(BASE + "user/2")
print(response.json())
input()

response= requests.delete(BASE + "user/1")
print(response)
