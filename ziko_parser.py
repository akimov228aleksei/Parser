import requests


def ziko_parser():
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
    # with open("ziko_file.json", "w", encoding='utf-8') as write_file:
    #     json.dump(ziko, write_file, ensure_ascii=False)
