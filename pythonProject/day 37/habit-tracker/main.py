import requests
from datetime import datetime

today = datetime.now()
x = today.strftime("%Y%m%d")



USERNAME = "hardikhd10"
TOKEN = "asccqf3qr43bfviqevwbffb"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "USERNAME": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# https://pixe.la/@hardikhd10
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_id = "sccevcnin1234"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param = {
    "id":graph_id,
    "name":"My Coding Graph",
    "unit":"Hours",
    "type":"float",
    "color":"momiji",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}
# https://pixe.la/v1/users/hardikhd10/graphs/sccevcnin1234.html

# graph_response = requests.post(url=graph_endpoint,json=graph_param,headers=headers)
# print(graph_response.text)

post_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"
value_param = {
    "date":x,
    "quantity":"10",
}
value_response = requests.post(url=post_value_endpoint,json=value_param,headers=headers)
print(value_response.text)