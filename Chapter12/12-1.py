import json
from urllib.request import urlopen
def getCountry(ipAdress):
    response = urlopen('http://ip-api.com/json/'+ipAdress).read().decode('utf-8')
    responsejson = json.loads(response)
    return responsejson.get('countryCode')

print(getCountry('50.78.253.58'))