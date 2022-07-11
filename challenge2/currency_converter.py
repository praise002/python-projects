import requests



# data = response.json()['result']

url = 'https://api.exchangerate.host/latest'
response = requests.get(url, timeout=5, params={
    "from": input(">Enter from currency code: ").upper(),
    "to": input(">Enter to currency code: ").upper(),
    "amount": input(">Enter amount: ")
})

# response = requests.get(url, timeout=5)
data = response.json()
# print(f"Converted amount: {data}")
# print(data['rates'].keys())
# print(data['rates'])
# print(type(data['rates']))
# print(dir(requests))
# print(data.keys())
print(data["rates"])
# for currency in data["rates"]:
#     print(currency)
for currency, exchange in data["rates"].items():
    # print(f"{currency}: {exchange}")
    print(f"Converted amount: {exchange}")
    break
# for i, j in data.items():
    # print(i)
    # print(i)
    # print(j)
    # for key, value in j:
    #     print(key)


