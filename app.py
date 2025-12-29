import requests
from requests.auth import HTTPBasicAuth

url = "https://prod.protectedtransactions.com/AUTH"

# UN-ENCODED payload
payload = "REQUEST=BT00610000000000000004D412E08008220000000000000040000000000000005011304270000050001"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "MyPythonClient/1.0",
    "Connection": "close"
}

response = requests.post(
    url,
    headers=headers,
    data=payload,
    auth=HTTPBasicAuth("datacap", "D8tk0p5y"),  # ← rotate immediately
    timeout=10,
    verify=True
)

print("Status:", response.status_code)
print("Body:", response.text)
