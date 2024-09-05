'''
contains functions to scrape data from oldlistings.com
'''
import re
from collections import defaultdict
# user packages


def get_oldlistings_property(p):
    '''
    p: a bs4 tag object
    return: a dictionary containing the information of a property
    '''
    # try to get data in json format
    info_dict = defaultdict(None)
    info_dict['lat'] = p.get('data-lat')
    info_dict['lng'] = p.get('data-lng')
    info_dict['rented_prices'] = []

    p = p.find('section', {'class':"grid-100 grid-parent"}) # replace p with its only (useful)child

    title = p.find('section', {'class':"grid-65 tablet-grid-65 clearfix"})
    # ad = p.find('section', {'class':"grid-35 tablet-grid-35 price"})
    list_of_history = p.find('section', {'class':"grid-100 historical-price"})


    # title
    info_dict['address'] = title.find('h2', {'class': 'address'}).text
    # other metadata: bed, bath, car etc
    # this do not garentee any structure of the data
    info_dict['meta_data'] = []
    for meta_data in title.find_all('p', {'class': re.compile("property-meta")}):
        obj = {}
        obj['label'] = meta_data.get('class')[1]
        obj['description'] = meta_data.find('span').text.split(' ')[0]
        obj['quantity'] = meta_data.contents[1].strip()
        info_dict['meta_data'].append(obj)


    # ad : we dont use ad

    # list of history
    for line in list_of_history.find('ul').find_all('li'):
        record = {}
        record['date'] = line.find('span').text
        record['price'] = line.contents[1]
        info_dict['rented_prices'].append(record)

    return info_dict

def get_oldlistings_page(soup):
    '''
    soup: a bs4 object containing the page
    return: a list of dictionaries containing the information of all properties in the page
    '''
    properties = soup.find('div', {'class':"content-col"}).findChildren("div" , recursive=False)
    list_of_properties = []
    for _property in properties:
        list_of_properties.append(get_oldlistings_property(_property))
        # get_info(property)
    return list_of_properties