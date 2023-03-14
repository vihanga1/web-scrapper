import requests
import json

def getDataFromServer(sku_array):
    r = requests.get('https://www.sample_url_.com').json()
        
    # adding skus to the sku_array
    for item in r:
        sku_array.append([item['content'], item['content1']])


# sending data to the server
def sendPricesToServer(array_for_server):
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

    r = requests.post("https://www.sample_url_.com", data=json.dumps(array_for_server), headers=headers)
    return r.json()