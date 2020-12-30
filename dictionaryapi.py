import requests
import json
import dpath.util

from requests import api

api_key = "8721864d05cc83948305bd4f843b2707"
application_id = "3993cc72"
word__to_lookup = input("Word: ")

word_lookup = requests.get(f"https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/{word__to_lookup}?fields=definitions&strictMatch=true", headers = {'app_id': application_id, 'app_key': api_key})
response = word_lookup.json()
#print(json.dumps(response, sort_keys=True, indent=4))

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values






#definition = str(response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
#print(definition)
#print(dpath.util.get(response, 'results/0/lexicalEntries/0/entries/0/senses/0/definitions/*'))
definitions = json_extract(response, 'id')
print(definitions)