import requests
import json
import time

# get access token for API (via email and password)
def get_accesstoken(email, password):
    headers = {
        'Authorization': 'Basic YzM2YjY3MjEtMDRkNS00ZGNlLWIxZjItNDc5NmQ4ZmNjODQ5Og==',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
    'grant_type': 'password',
    'username': email,
    'password': password
    }
    response = requests.post('https://api.yourpass.eu/oauth2/token', headers=headers, data=data)
    r = json.loads(response.text)
    return r

# create pass
def create_card(API_URL, token, name, card_nr, template):

    #name = name.encode('utf-8', 'ignore')

    headers = {
        'authorization': 'Bearer '+token,
        'content-type': 'application/json',
    }

    #data = '{"dynamicData":{"qrcode":"12345678","fullName":"Mr. Tom Cat","cardNumber":"12345678"},"dynamicImages":{"logo":"f5b3eabc-120e-4125-9d41-823d364cd4d0","icon":"0100ffe1-cc18-4a65-951d-6e032cf40765","strip": "224c0ab5-9582-4671-9594-0069f3457682"},"templateId":"a5bdefa4-9881-45a0-8c3d-b8bab679d8c7"}'
    data = '{"dynamicData":{"qrcode":"12345678","fullName":"'+name+'","cardNumber":"'+card_nr+'"},"templateId":"'+template+'"}'
    response = requests.post(API_URL+'/v1/pass', headers=headers, data=data)
    r = json.loads(response.text)
    return r

# get list of cards
def get_cards(API_URL, token):
    headers = {
        'authorization': 'Bearer '+token,
        'content-type': 'application/json',
    }
    params = (
        ('page', '1'),
        ('limit', '100'),
    )
    response = requests.get(API_URL+'/v1/pass', headers=headers, params=params)
    r = json.loads(response.text)
    return r

# delete card
def delete_card(API_URL, token, card_id):
    headers = {
        'authorization': 'Bearer '+token,
        'content-type': 'application/json',
    }
    response = requests.delete(API_URL+'/v1/pass/'+card_id, headers=headers)
    r = json.loads(response.text)
    return r

# update existing card / not working at the moment
def update_card(API_URL, token, card_id, name, card_nr, template):
    headers = {
        'authorization': 'Bearer '+token,
        'content-type': 'application/json',
    }
    data = '{"dynamicData":{"fullName":'+name+',"cardNumber":'+card_nr+'"},"templateId":'+template+'"}'#.encode('utf-8', 'ignore')

    response = requests.put(API_URL+'/v1/pass/'+card_id, headers=headers, data=data)
    r = json.loads(response.text)
    return r

# show single card
def read_card(API_URL, token, card_id):
    headers = {
    'authorization': 'Bearer '+token,
    'content-type': 'application/json',
    }
    response = requests.get(API_URL+'/v1/pass/'+card_id, headers=headers)
    r = json.loads(response.text)
    return r

# search for a single card
def search_card(API_URL, token, searchstring):
    headers = {
    'authorization': 'Bearer '+token,
    }
    params = (
        ('where', str('{"fullName":{"$like": "%'+searchstring+'%"}}')),
    )
    response = requests.get(API_URL+'/v1/pass/', headers=headers, params=params)
    r = json.loads(response.text)
    return r

# send push notification to all with same template
def push_notification(API_URL, token, template):
    headers = {
    'authorization': 'Bearer '+token,
    }
    response = requests.get(API_URL+'/v1/template/'+template+'/push', headers=headers)
    return response

# read template information
def read_template(API_URL, token, template):
    headers = {
    'authorization': 'Bearer '+token,
    }
    response = requests.get(API_URL+'/v1/template/'+template, headers=headers)
    r = json.loads(response.text)
    return r
