#Import the requests library
import requests

#Define the API endpoint where we’ll send the POST request
url = "https://reqres.in/api/users"

#payload is the dictionary we’re sending to the API (this will be turned into form data).
payload = {
    "name": "Alice",
    "job": "dev"
}

#We make a POST request to the URL with that data.
response =requests.post(url, data=payload)

#Converts the raw response into a Python dictionary
data =response.json()

#Print the response
print(data)