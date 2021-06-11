from pip._vendor import requests

class Crypto:

    def get_all(self):
        url = "https://coinranking1.p.rapidapi.com/coins"

        headers = {
            'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
            'x-rapidapi-host': "coinranking1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        data=response.json()
        data_1=data['data']['coins']
        return data_1