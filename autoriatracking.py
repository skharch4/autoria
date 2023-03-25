import requests

# define your requirements
make = "Toyota"
model = "Camry"
year_min = "2018"
price_max = "20000"

# make a request to the API
url = "https://developers.ria.com/auto/search"
params = {
    "api_key": "ia2nFHAfbae8MKBRKHyROJcqnK7v9O7LBszwPCwy",
    "marka_id": 75,
    "model_id": 59651,
    "s_yers": year_min,
    "price_to": price_max
}
response = requests.get(url, params=params)

# parse the JSON content
data = response.json()

# extract relevant data from the response
for car in data["result"]["search_result"]:
    title = f"{car['marka_name']} {car['model_name']} {car['title']}"
    link = f"https://auto.ria.com{car['link_to_view']}"
    price = f"{car['USD']} USD"

    # print the data or store it in a database
    print(f"{title} - {price} - {link}")
