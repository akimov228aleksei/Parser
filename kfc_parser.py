import requests


def kfc_parser():
    """
    A function that returns a description of all KFC restaurants
    """

    # Using the KFC API to get information
    response = requests.get('https://api.kfc.com/api/store/v2/store.get_restaurants',
                            params={'showClosed': 'true'})

    restaurants = response.json()['searchResults']

    kfc = []

    for restaurant in restaurants:

        address = restaurant['storePublic']['contacts']['streetAddress'].get('ru')
        latlon = restaurant['storePublic']['contacts']['coordinates']['geometry'].get('coordinates')
        name = restaurant['storePublic']['title'].get('ru')
        phone = restaurant['storePublic']['contacts']['phone'].get('number')

        if restaurant['storePublic']['status'] == 'Open':
            start_time = restaurant['storePublic']['openingHours']['regular']['startTimeLocal']
            end_time = restaurant['storePublic']['openingHours']['regular']['endTimeLocal']
            if start_time is not None and end_time is not None:
                working_hours = f'пн-вс {start_time[:-3]}-{end_time[:-3]}'
            else:
                working_hours = f'пн-вс {start_time}-{end_time}'
        else:
            working_hours = ['closed']

        kfc_dict = {
            'address': address,
            'latlon': latlon,
            'name': name,
            'phone': phone,
            'working_hours': working_hours
        }

        kfc.append(kfc_dict)

    return kfc
