from pip._vendor import requests
import json

class Todo:
    def get_5(self,name):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        querystring = {"q":name,"lat":"0","lon":"0","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

        headers = {
            'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
   
        return data
 