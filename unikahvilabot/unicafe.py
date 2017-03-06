# coding: utf-8
import datetime
import feedparser
feedparser.PREFERRED_XML_PARSERS.remove('drv_libxml2')


def restaurant_name(loc):
    names =[None,
            None,
            None,
       'Latin Market Metsätalo',
       'Olivia',
       None, 
       'Päärakennus',
       'Cafe Portaali',
       'Topelias',
       'Ylioppilasaukio',
       'Chemicum',          # 10
       'Exactum',
       'Physicum',
       'Meilahti']
    return names[loc]


def menu(loc):
    lang = 'eng'
    dow = datetime.date.today().weekday() # day of week
    query = 'http://messi.hyyravintolat.fi/rss/{lang}/{loc}'.format(lang=lang, loc=loc)
    d = feedparser.parse(query)
    menu_today = d['entries'][dow]['summary']
    menu_split = menu_today.split('. ')
    menu_items = menu_split[::2]
    #items_info = menu_split[1::2]
    return '\n'.join(menu_items)