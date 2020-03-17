from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tweepy as tw

bot_key = 'qBQwij3a0tmKOZjCWMBQdhmIR'
bot_skey = 'mso9fIvKJiX124nE8UlPQABrBKljtqKfsR8MkQtnV9gODbHqjD'
bot_token = '1044651780737576960-wRvKiUq5k1TwfiQdi5O2Xsk1NKKPBF'
bot_stoken = 'ImgpS09hNoYVExlVpUCMSGNqXy8ct5XQjNwxAbBzGuqYv'

auth = tw.OAuthHandler(bot_key, bot_skey)
auth.set_access_token(bot_token, bot_stoken)
api = tw.API(auth)

def CreateSearchString(filter):
    filt = ''
    for num,tbl in filter.items():
        filt += '('
        x = 0
        for key in tbl:
            x += 1
            filt += key
            if len(tbl) > x:
                filt += ' OR '
        filt += ') '
    filt += '-filter:retweets'
    return filt

def SearchUsingFilter(filter):

    results = tw.Cursor(api.search,q=CreateSearchString(filter), result_type = 'recent',lang="en").items(100)

    for tweet in results:
        loc = tweet.user.location
        if loc != "":
            print(loc)
            i=4
            while i>0: # Move all table entries down one.
                recentTweets[i] = recentTweets[i-1]
                i-=1


def LiveSearchUsingFilter(filter):  
    
    recentTweets = {}
    for i in range(100):
        recentTweets[i] = 0

    while (1):
        time.sleep(5)
        results = tw.Cursor(api.search,q=CreateSearchString(filter), result_type = 'recent',lang="en").items(5)
        for tweet in results:
            us = tweet.user
            isNewTweet = True  #   First assume it's a new tweet
            for k in recentTweets:
                if us == recentTweets[k] or us.location == "":  #   if the location is empty or the tweet has been found before
                    isNewTweet = False
            
            if isNewTweet:
                print(us.location)
                i=99
                while i>0: # Move all table entries down one.
                    recentTweets[i] = recentTweets[i-1]
                    i-=1
                recentTweets[0] = us # insert user into most recent position


# Stolen Objects

filters = {
    1:{'phone', 'wallet', 'keys', 'car', 'valuables', 'purse', 'identity'},
    2:{'stolen', 'stole'},
}

LiveSearchUsingFilter(filters)