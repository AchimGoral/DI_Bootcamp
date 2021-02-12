# response timer
import time
import requests

start = time.perf_counter()
requests.get('https://api.github.com') 
finish = time.perf_counter()
end_time = finish - start
print(f"Response time: {round(end_time, 6)} sec")


start = time.perf_counter()
requests.get('https://google.com') 
finish = time.perf_counter()
end_time = finish - start
print(f"Response time: {round(end_time, 6)} sec")

start = time.perf_counter()
requests.get('https://jpost.com') 
finish = time.perf_counter()
end_time = finish - start
print(f"Response time: {round(end_time, 6)} sec")

start = time.perf_counter()
requests.get('https://facebook.com') 
finish = time.perf_counter()
end_time = finish - start
print(f"Response time: {round(end_time, 6)} sec")