# twitter2rss.py
----------------
**Simple python script to parse twitter feed to generate a rss feed.**

 This simple script gets tweets from your timeline and publishes them as an rss feed.
 Attempts to fetch the content of the page using the readability algorithm 
 so that you can read the your twitter feeds anywhere Flipboard style

## Requires: 
* **tweepy**            | $ pip install tweepy            | https://github.com/tweepy/tweepy
* **python-feedgen**    | $ pip install feedgen           | https://github.com/lkiesow/python-feedgen
*  **readability-lxml**  | $ pip install readability-lxml  | https://github.com/buriy/python-readability 
*  **pytz**              | $ easy_install --upgrade pytz   | http://pytz.sourceforge.net/
*  **Other python libs** : pickle, urllib

 Created by: Ankit Shekhawat
 Website: http://www.ankit.ws

## USAGE: 
python tweet2rss.py
I use it with an hourly cronjob script

 Before running, edit settings.py for twitter account details 
 and the rss feed meta data details
 
 
## Todo
* Create an option for using readability api instead of readability-lxml.
