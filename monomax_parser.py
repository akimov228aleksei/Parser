import requests
from bs4 import BeautifulSoup


def monomax_parser():
    response = requests.get('https://monomax.by/map')
    monomax = []

    html_doc = response.content.decode('utf-8')

    # Getting part which contain information
    soup = BeautifulSoup(html_doc, 'html.parser')
    data = soup.find_all('script')[-1].text.replace(' ', '').strip()[157:-372].replace('newymaps.Placemark',
                                                                                   '').replace('\n', '')
    # Calculating record count
    amount = data.count('myPlacemark')
    points = []

    # Creating a list of dirty entries
    for i in range(amount):
        left_index = data.find(f"myPlacemark{i}=(")
        right_index = data.find("'})")
        points.append(data[left_index + 14:right_index + 2])
        data = data[right_index + 2:]

    # Clean the data from unnecessary tags
    for point in points:
        latlon = eval(point[:point.find('],') + 1])
        address = point[point.find(":'") + 2:point.find("',")]
        point = point[point.find("',") + 30:]
        phones = point[:point.find("',")]

        monomax_dict = {
            'address': address,
            'latlon': latlon,
            'phones': phones
        }

        monomax.append(monomax_dict)

    return monomax
