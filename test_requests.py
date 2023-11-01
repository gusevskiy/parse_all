import requests as req


url = "https://xn--e1abhgbth1ab1a.xn--p1ai/"

response = req.get(url)

print(response.text)