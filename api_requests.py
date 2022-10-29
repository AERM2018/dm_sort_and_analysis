import requests

from serializers import serializeDeaths
def getDeaths(limit):
    res = requests.get("http://localhost:3000/api/deaths?limit={}".format(limit))
    return serializeDeaths(res.json())
