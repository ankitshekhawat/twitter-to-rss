
# ADD your twitter Credentials and rename this file to settings.py

feed_item_limit = 1500
rss_file = 'rss.xml'
buffer_file= 'buffered_tweets.p'
log_file = 'session.log'

locale = 'UTC'

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
