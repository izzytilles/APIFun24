import requests # lib for making http requests
import json # lib for working with json

url = "https://flask-app-demo.onrender.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"

response = requests.get(url=url)

# first thing: check the status code
print(response.status_code)

if response.status_code == 200:
    # status is OK, we can extract prediction from response's JSON text
    json_object = json.loads(response.text)
    print(json_object)
    # must match key for key-value pair you're trying to extract the value of
    pred = json_object["prediction"]
    print("prediction:", pred)