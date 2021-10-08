import requests

isbn = "0-7475-3269-9"
key = f"ISBN:{isbn}"

# URL Structure
# <PROTOCOL>://<HOST>/<PATH>?<QUERY/PARAMS>

response = requests.get(
    "https://openlibrary.org/api/books",
    params={"format": "json", "bibkeys": key, "jscmd": "data"},
).json()

print(response)
