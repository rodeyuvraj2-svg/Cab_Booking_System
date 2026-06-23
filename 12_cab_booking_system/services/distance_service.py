import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImYwNjhiZDc4YmY2MzRkMmZiMmU3ZjJlMDY5NjU5MGViIiwiaCI6Im11cm11cjY0In0="


def get_coordinates(place):

    url = "https://api.openrouteservice.org/geocode/search"

    headers = {
        "Authorization": API_KEY
    }

    params = {
        "text": place
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    coords = data["features"][0]["geometry"]["coordinates"]

    return coords


def get_distance(pickup, drop):

    start = get_coordinates(pickup)
    end = get_coordinates(drop)

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            start,
            end
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    data = response.json()

    distance_meters = data["routes"][0]["summary"]["distance"]

    distance_km = round(
        distance_meters / 1000,
        2
    )

    return distance_km