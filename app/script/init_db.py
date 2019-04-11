import requests
import json

BASEURL = 'http://localhost:8000/'
PATH_TO_DATA = '/app/script/data/'

# generate token
data = {'username': 'admin', 'password': 'admin'}
r = requests.post(url=BASEURL + 'api-token-auth/', data=data)
token = r.json()['token']

headers = {'Authorization': 'Token ' + token,'Content-type': 'application/json'}

# language
with open(PATH_TO_DATA + 'language_labels.json', 'r') as f:
    language_label = json.load(f)

requests.post(BASEURL + 'api/language-labels/', headers=headers, data=json.dumps(language_label))

with open(PATH_TO_DATA + 'language_data.json', 'r') as f:
    language_data = json.load(f)

requests.post(BASEURL + 'api/language-datas/', headers=headers, data=json.dumps(language_data))


# confidentiality
with open(PATH_TO_DATA + 'confidentiality_labels.json', 'r') as f:
    confidentiality_label = json.load(f)

requests.post(BASEURL + 'api/confidentiality-labels/', headers=headers, data=json.dumps(confidentiality_label))

with open(PATH_TO_DATA + 'confidentiality_data.json', 'r') as f:
    confidentiality_data = json.load(f)

requests.post(BASEURL + 'api/confidentiality-datas/', headers=headers, data=json.dumps(confidentiality_data))


# doctype
with open(PATH_TO_DATA + 'doctype_labels.json', 'r') as f:
    doctype_label = json.load(f)

requests.post(BASEURL + 'api/doctype-labels/', headers=headers, data=json.dumps(doctype_label))

with open(PATH_TO_DATA + 'doctype_data.json', 'r') as f:
    doctype_data = json.load(f)

requests.post(BASEURL + 'api/doctype-datas/', headers=headers, data=json.dumps(doctype_data))

