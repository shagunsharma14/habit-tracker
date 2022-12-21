import requests
from datetime import datetime
# LINK = https://pixe.la/v1/users/bloodshot14/graphs/graph1.html
USERNAME = "bloodshot14"
TOKEN = "awtcy93crq4o37hiquw0fa"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
                "token": TOKEN,
                "username": USERNAME,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)
# print(response.status_code)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# GRAPH CREATION
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
# print(response.status_code)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

# POST HTTP REQUEST
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": input("How many kilometers did you cycle today? ")
}

# UPDATE HTTP REQUEST
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(response.text)
# print(response.status_code)

# DELETE HTTP REQUEST
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint,headers=header)
# print(response.status_code)