# third party module allows me to make requests
# like a browser
import requests
import json

# gives me system level controls in python
import sys

# i only want the user to be able to make one request
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

readable = response.json()

for result in readable["results"]:
    print(result["trackName"])
