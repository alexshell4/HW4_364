import requests
import json
from giphy_api_key import api_key

search_term = 'cats'
baseurl = "https://api.giphy.com/v1/gifs/search"
params = {'q':search_term, 'api_key':api_key, 'limit':5}
resp_obj = requests.get(baseurl, params=params)
resp_dict = json.loads(resp_obj.text)
print(resp_dict)
