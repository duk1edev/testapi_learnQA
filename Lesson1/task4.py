import requests

# response = requests.get("https://playground.learnqa.ru/api/hello?name=duk1e")
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
