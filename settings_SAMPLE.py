# -*- coding: utf-8 -*-
# ADD your twitter Credentials and rename this file to settings.py

feed_item_limit = 1500 # The rss feed tends to get really big so this prunes it
rss_file = 'rss.xml'
buffer_file= 'buffered_tweets.p' # buffer where the content is temporarily stored
log_file = 'session.log'

locale = 'UTC' # Change this to your locale to have the times show up in that locality

meta = {'id' : 'tweet2rss', 
        'title' : 'Twitter 2 RSS',
        'author' : {'name':'Tweet 2 rss','email':'jhonsmith@email.com'},
        'link' : 'http://example.com',
        'subtitle' : 'Converting twitter home timeline to rss feed',
        'link' : 'http://example.com/test.atom',
        'language' : 'en' }

twitter_keys = {'consumer_key' : 'xxxxxxxxxxxxxxxxxxxxxx',
                'consumer_secret' : 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'access_token' : 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'access_token_secret' : 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                }   


# If you want to use readablility.com's parser api (http://www.readability.com/developers/api/parser) 
# set using_readability_api to True, else it will use the cruder python readability-lxml library.
using_readability_api = True
readability_api_token = 'xxxxxxxxxxxxxxxxxxxxxx'