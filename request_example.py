import requests
url = "https://www.hltv.org/"
response = requests.get(url)
print(response.text)