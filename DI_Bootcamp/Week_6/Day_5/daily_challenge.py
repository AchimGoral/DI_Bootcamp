import requests
import json
from faker import Faker
f = Faker()

for _ in range(10):
	country = f.country()
	response = requests.get(f"https://restcountries.eu/rest/v2/name/{country}?fullText=true")
	data = json.loads(response.content)
	print(data)

	# data = json.loads(response)
	# print(data['name']['flag']['subregion']['population'])