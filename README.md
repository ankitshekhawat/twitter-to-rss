# Twitter to RSS feed generator
-----------------------
**twitter2rss.py is a simple python script to parse twitter feed to generate a rss feed.**

 This simple script gets tweets from your timeline and publishes them as an rss feed.
 Attempts to fetch the content of the page using the readability algorithm 
 so that you can read the your twitter feeds anywhere Flipboard style
 
 There is a choice of either using Readability.com's parser api or using python's readability-lxml.
 readability.com's api generates better and leaner results, but then adds dependency to an additional webservice.

## Requires: 
* **tweepy**            | $ pip install tweepy            | https://github.com/tweepy/tweepy
* **python-feedgen**    | $ pip install feedgen           | https://github.com/lkiesow/python-feedgen
*  **readability-lxml**  | $ pip install readability-lxml  | https://github.com/buriy/python-readability 
*  **pytz**              | $ easy_install --upgrade pytz   | http://pytz.sourceforge.net/
*  **Other python libs** : pickle, urllib

 Created by: Ankit Shekhawat
 Website: http://www.ankit.ws

## Usage: 
python tweet2rss.py
I use it with an hourly cronjob script

Before running, edit settings.py for twitter and readability account details 
and the rss feed meta data details
 
## Todo:
* Add an option to fetch tweets from a user list.
* Twitter sends tweets in reverse order. Need to reverse it by either seperating the fetching with parsing. or somehow from the twitter api itself.
* Base the pruning to something more intelligent than just feed limits, maybe from number of retweets.