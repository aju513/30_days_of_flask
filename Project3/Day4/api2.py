from pip._vendor import requests

class GlobalStats:
	def getGlobalstats(self):
		url = "https://coinranking1.p.rapidapi.com/stats"

		headers = {
		'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
		'x-rapidapi-host': "coinranking1.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers)
		getdata = response.json()["data"]
		return getdata