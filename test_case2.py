import requests
import json

input_data = [
    {"amount" : 15000.0, "currency" : "IDR"},
    {"amount" : 3.1, "currency" : "EUR"}
]
output_data = []

for data in input_data:
    amount = data["amount"]
    currency = data["currency"]
    response = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={currency}&to=USD')
    output_data.append(response.json()["rates"]["USD"])
    # print(json.dumps(response.json(), sort_keys=True, indent=4))

print("============== Input ===============")
print(json.dumps(input_data, sort_keys=True, indent=4))
print("============== Output ===============")
print(json.dumps(output_data, sort_keys=True, indent=4))
