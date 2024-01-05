import requests
import os

USERNAME = "oscar01"
GRAPH_ID = "graph01"
MY_TOKEN = os.environ.get("PixelaToken")

pixela_endpoint = "https://pixe.la/v1/users"
# --------------- Creates the account ------------------------

user_params = {
    "token": MY_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)

# ---------------- Creates the graph -------------------------
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN": MY_TOKEN
# }
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Walk Graph",
#     "unit": "mi",
#     "type": "int",
#     "color": "shibafu",
# }
#
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

# ------------------ Make a pixel ------------------------------
# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# header = {
#     "X-USER-TOKEN": MY_TOKEN
# }
#
# pixel_config = {
#     "date": "20240101",
#     "quantity": "5",
# }
#
# response = requests.post(url=pixel_endpoint, headers=header, json=pixel_config)
# print(response.text)

# --------------- Edit a pixel ----------------------------------
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240101"
#
# header = {
#     "X-USER-TOKEN": MY_TOKEN
# }
#
# pixel_config = {
#     "quantity": "1000",
# }
#
# response = requests.put(url=update_endpoint, headers=header, json=pixel_config)
# print(response.text)

# ------------ Delete a pixel ---------------------------------------
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240101"
#
# header = {
#     "X-USER-TOKEN": MY_TOKEN
# }
#
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
