import requests
from requests.auth import HTTPBasicAuth

url = "https://prodssl.protectedtransactions.com/AUTH"

headers = {
    "Connection": "close",
    "User-Agent": "MyPythonClient/1.0",
    "Host": "prodssl.protectedtransactions.com",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Request body (URL-encoded string literal)
payload = (
    "REQUEST%3DBT00610000000000000004D412E08008220000000000000040000000000000005011304270000050001"
)

# Path to your CA root certificate file
ca_cert_path = "ca_root.pem"   # Example: change to your actual file

response = requests.post(
    url,
    headers=headers,
    data=payload,
    auth=HTTPBasicAuth("datacap", "D8tk0p5y"),
    verify=ca_cert_path  # Use your own CA certificate
)

print("Status Code:", response.status_code)
print("Response Body:")
print(response.text)
