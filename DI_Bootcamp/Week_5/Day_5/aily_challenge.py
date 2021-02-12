# response timer

import requests 
  
response_get = requests.get('https://api.github.com') 
print(response_get) 
print(response_get.elapsed)

response_get = requests.get('https://google.com') 
print(response_get) 
print(response_get.elapsed)

response_get = requests.get('https://jpost.com') 
print(response_get) 
print(response_get.elapsed)