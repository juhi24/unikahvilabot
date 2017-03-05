# coding: utf-8
import feedparser

lang = 'eng'
dow = 0 # day of week

loc = [None,
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
query = 'http://messi.hyyravintolat.fi/rss/{lang}/{loc}'.format(lang=lang, loc=10)

d = feedparser.parse(query)
menu = d['entries'][dow]['summary']