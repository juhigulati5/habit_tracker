import requests
from datetime import datetime

USERNAME = "jujubee"
TOKEN = "fkgfkfgkfkfg"
GRAPH_ID = "graph1"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# POST - creates something

# Create account
response = requests.post(url=pixela_endpoint, json=user_params)
response.raise_for_status()
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Create graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": DATE,
    "quantity": input("How many pages did you read today? "),
}

# Create pixel
response = requests.post(url=create_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

update_config = {
    "quantity": "30"
}

# PUT - adds to something that has already been created

# Update pixel
response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
print(response.text)

# DELETE - deletes something

# Delete pixel
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)