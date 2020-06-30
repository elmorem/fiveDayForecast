import requests
import click


def cli():
    url= 'https://api.weatherbit.io/v2.0/current'
    querystring = {"lang":"en", "units":"I" ,"postal_code":95616, "key": '7949beb29157403590852a48639efb2c'}
    headers = {
        "content-type": "application/json; charset=utf-8"
    }
    #response = requests.get('https://api.weatherbit.io/v2.0/current', params=querystring)
    response = requests.get(url, params=querystring)

    json_response=response.json()
    
    temp=json_response['data'][0]['temp']
    city=json_response['data'][0]['city_name']
    
    print(f"The temperature in {city} right now is {temp}.")

    #f-string "The temperature in Davis right now is {}."


