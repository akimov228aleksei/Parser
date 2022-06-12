import requests


def ziko_parser():
    """
    A function that returns a description of all pharmacies
    """

    # Using the ziko API to get information
    response = requests.get('https://www.ziko.pl/wp-admin/admin-ajax.php',
                            params={'action': 'get_pharmacies'})
    pharmacies = response.json()

    ziko = []

    for pharmacy in pharmacies:
        address = pharmacies[pharmacy]['address']
        latlon = [pharmacies[pharmacy]['lat'], pharmacies[pharmacy]['lng']]
        name = pharmacies[pharmacy]['title']
        working_hours = pharmacies[pharmacy]['hours'].replace('<br>', '').splitlines()

        ziko_dict = {
            'address': address,
            'latlon': latlon,
            'name': name,
            'working_hours': working_hours
        }

        ziko.append(ziko_dict)

    return ziko
