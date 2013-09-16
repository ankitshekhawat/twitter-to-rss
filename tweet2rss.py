# tweet2rss.py
#
#
# Thia simple script gets tweets from your timeline and publishes them as an rss feed.
# Attempts to fetch the content of the page using the readability algorithm 
# so that you can read the your twitter feeds anywhere Flipboard style
# 
# 
# 
#
# Requires: 
# tweepy            | $ pip install tweepy            | https://github.com/tweepy/tweepy
# python-feedgen    | $ pip install feedgen           | https://github.com/lkiesow/python-feedgen
# readability-lxml  | $ pip install readability-lxml  | https://github.com/buriy/python-readability 
# pytz              | $ easy_install --upgrade pytz   | http://pytz.sourceforge.net/
#
#
# Created by: Ankit Shekhawat
# Website: http://www.ankit.ws
#
# USAGE: python tweet2rss.py
#
# Before running, edit settings.py for twitter account details 
# and the rss feed meta data details
#

import pickle
import tweepy
from feedgen.feed import FeedGenerator
from readability.readability import Document
import urllib
import pytz
from settings import *
from logger import Logger

log = Logger(log_file, locale)
log.set_level_to('DEBUG')

def load_buffer(fileName):
    try:
        buffered = pickle.load( open( fileName, "rb" ) )
    except Exception, e:
        log.error("[Buffer_Load_ERR]:  Unable to load tweets from buffered. It's possible that the script is running for the first time. In that case it will be generated at the end of the script")
        buffered =[]
    else:
        log.info("Buffer loaded successfully with " + str(len(buffered)) + " tweets.")
    return buffered

def get_lastID(buffered):
    id_list =[]
    for tweet in buffered:
        id_list.append(tweet['id'])
    return max(id_list)

def parse_twitter(buffered, keys):
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)

    # If the authentication was successful, you should
    # see the name of the account print out
    log.debug('Fetching feeds for twitter user: ' + api.me().name) 

    try: # In case the script is running for the first time. fetch the 
        lastID = get_lastID(buffered)

    except Exception, e:
        log.warn('Can not retreive last ID, retreiving last 200 tweets instead')
        pub = api.home_timeline(count=200) #fetch feeds without since ID   
        for i in pub:
            parse_tweet(i)

    else:
        log.debug("Will fetch tweets since tweet ID " + str(lastID))
        for i in tweepy.Cursor(api.home_timeline, since_id=str(lastID)).items(): 
            parse_tweet(i)
                # old code:  pub = api.home_timeline(count=200, since_id=str(lastID) ) #fetch feeds from the last ID
           
    return buffered

def parse_tweet(i):
    tweet ={}
    s = i.entities['urls']
    if len(s) > 0: # Check if tweet has a url
        urls = s[0]
        tweet['url'] = urls['expanded_url']
        
        try:
            html = urllib.urlopen(tweet['url']).read()
            tweet['readable_title'] = Document(html).title().encode('utf-8')
            tweet['readable_article'] = Document(html).summary().encode('utf-8')
        except Exception, e:
            log.error(e.message + ' ' + e.reason)

        else:
            tweet['text'] = i.text.encode('utf-8')
            tweet['screen_name'] = i.user.screen_name
            tweet['profile_image_url'] = i.user.profile_image_url
            tweet['user_name'] = i.user.name
            tweet['user_url'] = i.user.url
            tweet['id'] = i.id
            tweet['id_str'] = i.id_str
            tweet['created_at'] = i.created_at
            
            try:
                log.debug(tweet['id_str'].decode('utf-8', 'replace') + ' : @' + tweet['screen_name'].decode('utf-8', 'replace') + ' : ' + tweet['text'].decode('utf-8', 'replace'))
            except Exception, e:
                log.error(e.message + ' ' + e.reason)
                
            
            try: #adding tweet context on top of the parsed article
                article_header =  '<img src="'.decode('utf-8') + tweet['profile_image_url'].decode('utf-8') + '" alt="'.decode('utf-8') + tweet['screen_name'].decode('utf-8') + '" /><p><strong>'.decode('utf-8') + tweet['user_name'].decode('utf-8') + ': </strong>'.decode('utf-8') + tweet['text'].decode('utf-8') +'</p>'.decode('utf-8')
            except Exception, e:
                log.error(e.message + ' ' + e.reason)
            else:
                tweet['readable_article'] = article_header.encode('utf-8') + tweet['readable_article']

            buffered.insert(0, tweet)
            del buffered[feed_item_limit:] #pruning the feed to a maximum number of feeds.
            pickle.dump( buffered, open( buffer_file, "wb" ) )
            

def generateFeeds(buffered, meta):
    utc = pytz.utc
    fg = FeedGenerator()
    fg.id(meta['id'])
    fg.title(meta['title'])
    fg.author(meta['author'])
    fg.subtitle(meta['subtitle'])
    fg.link( href=meta['link'], rel='self' )
    fg.language(meta['language'])

    for tweet in buffered:
        fe = fg.add_entry()
        fe.id(tweet['url'].decode('utf-8'))
        fe.published(utc.localize(tweet['created_at']).astimezone(pytz.timezone(locale)))
        fe.link = {tweet['url'].decode('utf-8')}
        fe.guid(tweet['url'].decode('utf-8'))
        fe.title(tweet['readable_title'].decode('utf-8'))
        fe.description(tweet['readable_article'].decode('utf-8'))
        fe.author({'name': tweet['user_name'].decode('utf-8'), 'email':tweet['user_url'].decode('utf-8')})
    return fg                    

def write_rss(feedGenerator, fileName): 
    log.debug('Writing RSS file')
    try:
        feedGenerator.rss_file('fileName') # Write the RSS feed to a file
    except Exception, e:
        log.error(e.message + ' ' + e.reason)
    else:
        log.info('RSS file ' + fileName + " written successfully.")

log.info('Session Started')
buffered = load_buffer(buffer_file)
parsed = parse_twitter(buffered, twitter_keys)
feed = generateFeeds(parsed, meta)
write_rss(feed, rss_file)
log.info('Session Finished\n\n')
