import requests

# Define the URL to which you want to send the POST request
url = 'https://api.chessnoor.com/post'

# Define the data you want to send in the request (in this example, a JSON payload)
payload = {
    "title": "hellllo world"
    
}

# Send the POST request with the defined URL and payload
response = requests.post(url, json=payload, headers= {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxNzE0MjE5NzI1NjYwIiwiZW1haWwiOiJhc2RAdmF1bHQuY29tIiwidXNlcklkIjoiNjYyY2VhY2QxNmIzZGM1M2ZiYTUzZDkxIiwiaWF0IjoxNzE0Mjk5NjY2LCJleHAiOjE3MTQzMDg2NjZ9.NRd3d0AWMjVtk6cBfUO6B6Zlkh4PbnLPUYHcqGGg0TQ'})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print('POST request successful!')
    print('Response:', response.json())  # Assuming the response is in JSON format
else:
    print('POST request failed with status code:', response.status_code)