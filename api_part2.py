import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

print("=== GET ===")
r = requests.get(url)
print("Status:", r.status_code)
print(json.dumps(r.json()[:2], indent=2))

print("\n=== POST ===")
data = {
    "title": "devasc",
    "body": "part 2",
    "userId": 1
}
r2 = requests.post(url, json=data)
print("Status:", r2.status_code)
print(json.dumps(r2.json(), indent=2))
