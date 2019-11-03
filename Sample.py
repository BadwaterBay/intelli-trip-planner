import requests

api_key = 'AIzaSyDtZvRnTEtBj8SP7tClaNxJRx5lrwmVASE'
api_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
origin = '30.289029, -97.735392'
destinations = [
    '30.399866, -97.686537',
    '30.291369, -97.728205',
    '30.359284, -97.733981',
    '30.336613, -97.717674',
    '30.557494, -97.690022'
]


def get_travel_time(destination):
    params = {'origins': origin, 'destinations': destination, 'key': api_key, 'units': 'imperial'}
    r = requests.get(url=api_endpoint, params=params)
    result = r.json()
    return result['rows'][0]['elements'][0]['duration']['text']


travel_times = [get_travel_time(d) for d in destinations]
print(travel_times)