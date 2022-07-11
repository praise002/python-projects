import requests

url = 'https://api.exchangerate.host/latest'
response = requests.get(url, timeout=5, params={
    "base": "USD",
    "symbols": "ZAR", "NGN"
    "to": input(">Enter to currency code: ").upper(),
    "amount": input(">Enter amount: ")
})

data = response.json()
print(data["rates"])

for currency, exchange in data["rates"].items():
    # print(f"{currency}: {exchange}")
    print(f"Converted amount: {exchange}")
