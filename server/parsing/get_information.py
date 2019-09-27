from bs4 import BeautifulSoup


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    organizations = soup.find(
        'div', class_='block_places').findAll('div', class_='block_place')
    result_organizations = []
    for organization in organizations:
        city = organization.find('div', class_='block_place_city').text
        name = organization.find('div', class_='block_place_name').text
        adress = organization.find('div', class_='block_place_address').text
        result_organizations.append({
            'city': city,
            'name': name,
            'adress': adress,
        })
    return result_organizations
